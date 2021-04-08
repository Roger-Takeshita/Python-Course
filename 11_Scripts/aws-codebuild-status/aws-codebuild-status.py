
#! Developed by Roger Takeshita
#! https://github.com/Roger-Takeshita

import boto3
import botocore
import sys


class colors:
    BL = '\u001b[38;5;4m'
    OG = '\u001b[38;5;202m'
    GN = '\u001b[38;5;28m'
    RD = '\u001b[38;5;160m'
    WT = '\u001b[37;1m'
    RST = '\u001b[0m'
    BGGN = '\u001b[48;5;28m'
    BGOG = '\u001b[48;5;172m'
    BGRD = '\u001b[48;5;160m'


class format:
    BOLD = '\u001b[1m'
    RST = '\u001b[0m'


def printStatus(build):
    project_name = build['projectName']
    start_time = build['startTime']
    start_time = build['startTime']
    end_time = build['endTime']
    build_number = build['buildNumber']
    phase = build['currentPhase']
    status = build['buildStatus']

    print(f'  {colors.BL}{project_name}{colors.RST}')
    print()
    print(f'     Attempt:    {colors.BL}{build_number}{colors.RST}')
    print(f'     Start Time: {colors.BL}{start_time}{colors.RST}')
    print(f'     End Time:   {colors.BL}{end_time}{colors.RST}')

    if phase == 'COMPLETED':
        print(f'     Phase:      {colors.GN}{phase}{colors.RST}')
    else:
        print(f'     Phase:      {colors.OG}{phase}{colors.RST}')
    if status == 'SUCCEEDED':
        print(
            f'     Status:     {colors.BGGN}{colors.WT}{format.BOLD}{status}{colors.RST}')
    elif status == 'FAILED':
        print(
            f'     Status:     {colors.BGRD}{colors.WT}{format.BOLD}{status}{colors.RST}')
    else:
        print(
            f'     Status:     {colors.BGOG}{colors.WT}{format.BOLD}{status}{colors.RST}')
    print()


def getArgs():
    try:
        if len(sys.argv) > 2:
            return {'profile_name': sys.argv[1], 'last_build': sys.argv[2]}

        return {'profile_name': sys.argv[1], 'last_build': ''}
    except IndexError:
        print()
        print(
            f'     {colors.BGRD}{colors.WT} ERROR: {colors.RST} Please provide an aws profile.')
        print()
        exit()


def getBuildStatus(profile):
    session = boto3.Session(profile_name=profile['profile_name'])
    codebuild = session.client('codebuild')

    res_builds = codebuild.list_builds()
    res_projects = codebuild.list_projects()
    projects_array = res_projects['projects']
    res_builds = codebuild.batch_get_builds(ids=res_builds['ids'])
    builds_array = res_builds['builds']
    builds = {}

    for build in builds_array:
        project = build['projectName']
        if project not in builds.keys():
            builds.update({project: {
                'projectName': project,
                'startTime': build['startTime'],
                'endTime': build['endTime'],
                'buildNumber': build['buildNumber'],
                'currentPhase': build['currentPhase'],
                'buildStatus': build['buildStatus']
            }})

    print()

    if profile['last_build'] == '-a' or profile['last_build'] == '--all':
        for project in projects_array:
            build = builds[project]
            printStatus(build)
    else:
        build = builds[projects_array[0]]
        printStatus(build)


def getStatus(profile):
    try:
        getBuildStatus(profile)
    except botocore.exceptions.ParamValidationError:
        print()
        print(
            f"     {colors.BGOG}{colors.WT} WARNING: {colors.RST} The config profile ({colors.BL}{profile['profile_name']}{colors.RST}) doesn't have builds.")
        print()
    except botocore.exceptions.ProfileNotFound:
        print()
        print(
            f"     {colors.BGRD}{colors.WT} ERROR: {colors.RST} The config profile ({colors.BL}{profile['profile_name']}{colors.RST}) could not be found.")
        print()


if __name__ == "__main__":
    profile = getArgs()
    getStatus(profile)
