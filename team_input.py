

def parse_team_file(filename):
    with open(filename, 'r') as team_file:
        file_content = team_file.read()
    teams = []
    for line in file_content.split('\n'):
        if line == '':
            continue
        if line.count('&') != 1:
            raise AttributeError('The input file is invalid, every line should contain only one &')
        teams.append([team.strip() for team in line.split('&')])
    return teams
