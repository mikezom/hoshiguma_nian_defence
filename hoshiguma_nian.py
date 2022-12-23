import csv

HOSHIGUMA_STATS_AT_LEVEL = {
    30: (3150, 651),
    60: (3513, 717),
    90: (3850, 783)
}
HOSHIGUMA_SKILL_DATA = {
    1: {
        7: (26, 44, 0.65),
        8: (27, 43, 0.7),
        9: (28, 42, 0.75),
        10: (30, 40, 0.8)
    },
    2: {
        7: (0, 0, 0.21),
        8: (0, 0, 0.24),
        9: (0, 0, 0.27),
        10: (0, 0, 0.3)
    },
    3: {
        7: (25, 54, 0.6),
        8: (25, 53, 0.7),
        9: (25, 52, 0.8),
        10: (25, 50, 0.9)
    }
}
HOSHIGUMA_MODULE_DATA = {
    'N': {
        0: (0, 0, 0.06, 0)
    },
    'Y': {
        1: (0, 70, 0.06, 0),
        2: (0, 90, 0.06, 0),
        3: (0, 100, 0.06, 0)
    },
    'X': {
        1: (125, 85, 0.06, 0.2),
        2: (165, 115, 0.15, 0.2),
        3: (200, 140, 0.17, 0.2),
    }
}
NIAN_SKILL_DATA = {
    0: {
        0: (0, 0, 0)
    },
    2: {
        7: (32, 50, 1),
        8: (33, 50, 1.1),
        9: (34, 50, 1.2),
        10: (35, 50, 1.3)
    }
}
NIAN_STAT_AT_LEVEL = {
    30: (3450, 663),
    60: (3775, 730),
    90: (4099, 796)
}
NIAN_MODULE_DATA = {
    'N': {
        0: (0, 0, 0.16, 0, 0)
    },
    'X': {
        1: (200, 60, 0.16, 0.2, 0),
        2: (280, 70, 0.16, 0.2, 0.15),
        3: (375, 80, 0.16, 0.2, 0.21)
    }
}
result = []
# An elements looks like
# (Name, Level, Skill, SkillLevel, SkillDurance, SkillCoolDown, Module, ModuleLevel, ActualHP, ActualDefence)
for level, (hp, defence) in HOSHIGUMA_STATS_AT_LEVEL.items():
    for skill, skill_data in HOSHIGUMA_SKILL_DATA.items():
        for module, module_data in HOSHIGUMA_MODULE_DATA.items():
            for skill_level, (skill_durance, skill_cooldown, skill_defence_boost) in skill_data.items():
                for module_level, (module_hp_boost, module_defence_boost, module_talant, module_additional_talent) in module_data.items():
                    if level < 60 and module_level > 0:
                        continue
                    actual_hp = hp + module_hp_boost
                    actual_defence = (defence + module_defence_boost) * (1 + skill_defence_boost + module_talant + module_additional_talent)
                    new_element = ['hoshiguma', level, skill, skill_level, skill_durance, skill_cooldown, module, module_level, actual_hp, actual_defence]
                    result.append(new_element)

for level, (hp, defence) in NIAN_STAT_AT_LEVEL.items():
    for skill, skill_data in NIAN_SKILL_DATA.items():
        for module, module_data in NIAN_MODULE_DATA.items():
            for skill_level, (skill_durance, skill_cooldown, skill_defence_boost) in skill_data.items():
                for module_level, (module_hp_boost, module_defence_boost, module_talant_hp, module_additional_talent, module_additional_defence) in module_data.items():
                    if level < 60 and module_level > 0:
                        continue
                    actual_hp = (hp + module_hp_boost) * (1 + module_talant_hp)
                    actual_defence = (defence + module_defence_boost) * (1 + skill_defence_boost + module_additional_talent + module_additional_defence)
                    new_element = ['nian', level, skill, skill_level, skill_durance, skill_cooldown, module, module_level, actual_hp, actual_defence]
                    result.append(new_element)

fields = ['Name', 'Level', 'Skill', 'SkillLevel', 'SkillDurance', 'SkillCoolDown', 'Module', 'ModuleLevel', 'ActualHP', 'ActualDefence']

with open('hoshiguma_nian.csv', 'w+') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(result)