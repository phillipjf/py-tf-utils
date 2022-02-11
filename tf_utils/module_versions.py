import os
import re
import urllib
from urllib import request
import subprocess
from typing import Optional

from tf_utils import utils


def find_module_sources(root):
    modules_source = utils.module_file_list(root)
    modules = {}
    for mod_root, files in modules_source.items():
        for f in files:
            file_path = os.path.join(mod_root, f)
            tf_definitions = utils.load_terraform(file_path)
            for m in tf_definitions.get("module", []):
                mod_map = list(m.values())[0]
                modules[list(m.keys())[0]] = {
                    'source': mod_map.get("source", [''])[0],
                    'version': mod_map.get("version", [''])[0]
                }

    git_sources = re.compile(r'^(git::|github.com|git@github.com|bitbucket.org)')
    mercurial_sources = re.compile(r'^(hg::)')
    archive_sources = re.compile(r'.*(\.(zip|tar\.bz2|tbz2|tar\.gz|tgz|tar.xz|txz))|(.*archive=.*)$')
    s3_sources = re.compile(r'^(s3::)')
    gcs_sources = re.compile(r'^(gcs::)')
    for mod, info in modules.items():
        if info['version']:  # registry
            info['source_type'] = 'registry'
            info['latest_version'] = 'not_supported'
        elif info['source'].startswith('./') or info['source'].startswith('../'):  # local
            info['source_type'] = 'local'
            info['version'] = 'latest'
            info['latest_version'] = 'latest'
        elif re.match(git_sources, info['source']):  # git
            info['source_type'] = 'git'
            source_url = info['source'].removeprefix('git::')
            url_parts = urllib.parse.urlparse(source_url)
            if url_parts.netloc == '':
                source_url = f"https://{source_url}"
                url_parts = urllib.parse.urlparse(source_url)
            qp = {}
            for q in url_parts.query.split('&'):
                qk, qv = q.split('=')
                qp[qk] = qv
            info['version'] = qp.get('ref', 'not_supported')
            info['latest_version'] = get_latest_tag(url_parts)
        elif re.match(mercurial_sources, info['source']):  # mercurial
            info['source_type'] = 'mercurial'
            source_url = info['source'].removeprefix('hg::')
            url_parts = urllib.parse.urlparse(source_url)
            if url_parts.netloc == '':
                source_url = f"https://{source_url}"
                url_parts = urllib.parse.urlparse(source_url)
            qp = {}
            for q in url_parts.query.split('&'):
                qk, qv = q.split('=')
                qp[qk] = qv
            info['version'] = qp.get('ref', 'not_supported')
            info['latest_version'] = 'not_supported'
        elif re.match(archive_sources, info['source']):  # archive
            info['source_type'] = 'archive'
            info['version'] = 'not_supported'
            info['latest_version'] = 'not_supported'
        elif re.match(s3_sources, info['source']):  # s3
            info['source_type'] = 's3'
            info['version'] = 'not_supported'
            info['latest_version'] = 'not_supported'
        elif re.match(gcs_sources, info['source']):  # gcs
            info['source_type'] = 'gcs'
            info['version'] = 'not_supported'
            info['latest_version'] = 'not_supported'
        else:
            info['source_type'] = 'unknown'
            info['version'] = 'not_supported'
            info['latest_version'] = 'not_supported'

    return modules


def get_latest_tag(repo_url: urllib.parse.ParseResult) -> Optional[str]:
    latest_tag = 'not_supported'
    # Since ssh urls will contain a 'git@', we need to strip that to build the https url
    netloc = repo_url.netloc if '@' not in repo_url.netloc else repo_url.netloc.split('@')[1]
    # The https url does not need to care about params, query, or fragment
    https_url = urllib.parse.urlunparse(('https', netloc, repo_url.path, None, None, None))
    try:
        request.urlopen(https_url)
    except request.HTTPError:
        # if the url returns an error, skip
        return 'http_error'

    # This implies a dependency on git being installed on the host machine
    out = subprocess.run(
        f"git ls-remote --tags --refs --sort=v:refname {https_url} | cut -f2",
        shell=True,
        capture_output=True
    )
    # If all goes well, filter the tags to the last one
    if out.returncode == 0:
        tags = list(filter(None, out.stdout.decode("utf-8").split("\n")))
        if len(tags) > 0:
            latest_tag = tags[-1]
    return latest_tag


def print_module_versions(root: str):
    modules = find_module_sources(root)
    col_1_len = len(max(modules.keys(), key=len)) + 2
    print(f"{'module':<{col_1_len}}{'module type':<12}{'current version':<20}{'latest version':<20}")
    for name, info in modules.items():
        print(f"{name:<{col_1_len}}{info['source_type']:<12}{info['version']:<20}{info['latest_version']:<20}")
