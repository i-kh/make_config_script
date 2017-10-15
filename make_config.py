import os
import argparse


def collect_env_properties(env_prefix, excluded_sections=None,
                           excluded_variables=None, excluded=None):
    """

    :param env_prefix: Environement prefi name
    :type env_prefix: str
    :param excluded_sections: Names ot the sections excluded
    :param excluded_variables: Names of the variables excluded
    :param excluded: Full names of variables excluded
                    [ENV_PREFIX_SECTION_NAME_VARIABLE_NAME]
    :return:
    """
    props = {}
    excluded = excluded or []
    excluded_sections = list(map(lambda s: s.lower(),
                                 (excluded_sections or '').split(',')))
    excluded_variables = list(map(lambda s: s.lower(),
                                  (excluded_variables or '').split(',')))

    for (env_name, val) in os.environ.items():
        if env_name not in excluded and env_name.startswith(env_prefix):
            section_prop_name = env_name[len(env_prefix):].lower()
            section_name = section_prop_name.split('_')[0]
            if section_name in excluded_sections: continue
            section_name_len = len(section_name)
            prop_name = section_prop_name[section_name_len + 1:]
            if prop_name in excluded_variables: continue
            props.setdefault(section_name, {})
            props[section_name][prop_name] = val
    return props


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prefix', help='Environment variables prefix',
                        required=True)
    parser.add_argument(
        '-exc', '--excluded',
        help=('Excluded properties fullnames '
              '[ENV_PREFIX_SECTION_NAME_VARIABLE_NAME]'))
    parser.add_argument('-es', '--excluded_sections',
                        help='Excluded properties names [VARIABLE_NAME]')
    parser.add_argument('-ev', '--excluded_variables',
                        help='Excluded section names [SECTION_NAME]')
    args = parser.parse_args()
    make_file(collect_env_properties(args.prefix,
                                     excluded=args.excluded,
                                     excluded_variables=args.excluded_variables,
                                     excluded_sections=args.excluded_sections))


def make_file(d):
    with open('conf.ini', mode='w+') as f:
        for section, section_val in d.items():
            f.write('[{section_name}]\n'.format(section_name=section))
            for key, val in section_val.items():
                f.write('{key} = {val}\n'.format(key=key, val=val))
            f.write('\n')


main()