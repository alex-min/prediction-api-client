
class TeamInputException(Exception):
    pass

def parse_team_file(filename):
    with open(filename, 'r') as team_file:
        file_content = team_file.read()
    teams = []
    for line in file_content.split('\n'):
        if line == '':
            continue
        if line.count('&') != 1:
            error = 'The input file {} is invalid, every line should contain only one &'.format(filename)
            raise TeamInputException(error)
        teams.append([team.strip() for team in line.split('&')])
    return teams
