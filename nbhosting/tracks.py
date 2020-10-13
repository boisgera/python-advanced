# pylint: disable=c0111

from nbhosting.courses import (
    Track, Section, Notebook,
    notebooks_by_patterns, track_by_directory)

def tracks(coursedir):
    """
    coursedir is a CourseDir object that points
    at the root directory of the filesystem tree
    that holds notebooks

    result is a list of Track instances
    """

    track_specs = [
        ('Python avancé', 'Python avancé', 'python', [
            ('1/9: jeux', 'notebooks/1-*.md', 'tps/games/README.md'),
            ('2/9: types de base', 'quiz/2*.md', 'notebooks/2-*.md', 'tps/dijkstra/README.md'),
            ('3/9: itérations', 'quiz/3*.md', 'notebooks/3-*.md'),
            ('4/9: fonctions', 'quiz/4*.md', 'notebooks/4-*.md'),
            ('5/9: ???', 'quiz/5*.md', 'notebooks/5-*.md'),
            ('6/9: ???', 'quiz/6*.md', 'notebooks/6-*.md'),
            ('7/9: ???', 'quiz/7*.md', 'notebooks/7-*.md'),
            ('8/9: ???', 'quiz/8*.md', 'notebooks/8-*.md'),
            ('9/9: ???', 'quiz/9*.md', 'notebooks/9-*.md'),
        ])]

    return [Track(coursedir,
                  [Section(coursedir=coursedir,
                           name=section_name,
                           notebooks=notebooks_by_patterns(
                               coursedir, patterns))
                   for section_name, *patterns in section_specs],
                  name=track_name,
                  description=track_description,
                  id=track_id)
            for (track_name, track_description, track_id, section_specs) in track_specs]
