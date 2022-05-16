import json
from pprint import pprint as pp

from config import DATA_PATH



def _load_data(path=DATA_PATH):
    """ Загружает данные про кандидатов """
    with open(path, "r", encoding="utf=-8") as file:
        data = json.load(file)
        return data

def candidates_get_all():
    """ Получает список всех кандидатов """
    data = _load_data()
    return data

def candidates_get_by_pk(pk):
    """Получаем кандидата по его PK"""
    candidates = _load_data()
    for candidate in candidates:
        if candidate["id"] == pk:
            return candidate

def candidate_get_by_skill(skill_name):
    """Получать кандидатов по навыкам"""

    skilled_candidates = []
    skill_name_lower = skill_name.lower()

    candidates = _load_data()
    for candidate in candidates:
        skills = candidate["skills"].strip().lower().split(", ")
        if skill_name_lower in skills:
            skilled_candidates.append(candidate)
            continue
    return skilled_candidates







#pp(candidate_get_by_skill("html"))
