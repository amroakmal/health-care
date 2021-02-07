COVID_SYMP_COUNT = 3
HEART_ATTACK_SYMP_COUNT = 8
STROKE_SYMP_COUNT = 12

users = []

def CHECK_HEART_ATTACK(symp):
    cnt = 0
    if symp == 'chest pain':
        cnt += 1
    elif symp == 'light headed':
        cnt += 1
    elif symp == 'feel weak':
        cnt += 1
    elif symp == 'discomfort in jaw':
        cnt += 1
    elif symp == 'discomfort in neck':
        cnt += 1
    elif symp == 'pain in arms':
        cnt += 1
    elif symp == 'pain in shoulders':
        cnt += 1
    elif symp == 'shortness of breath':
        cnt += 1
    return cnt


def CHECK_COVID(symp):
    cnt = 0
    if symp == 'short breath':
        cnt += 1
    elif symp == 'can smell':
        cnt += 1
    elif symp == 'sore throat':
        cnt += 1
    return cnt


def CHECK_STROKE(symp):
    cnt = 0
    if symp == 'sudden numbness':
        cnt += 1
    if symp == 'weakness':
        cnt += 1
    if symp == 'sudden numbness':
        cnt += 1
    if symp == 'sudden confusion':
        cnt += 1
    if symp == 'trouble speaking':
        cnt += 1
    if symp == 'difficulty understanding speech':
        cnt += 1
    if symp == 'sudden trouble seeing':
        cnt += 1
    if symp == 'sudden trouble walking':
        cnt += 1
    if symp == 'dizziness':
        cnt += 1
    if symp == 'loss of balance':
        cnt += 1
    if symp == 'lack of coordination':
        cnt += 1
    if symp == 'sudden severe headache':
        cnt += 1
    return cnt


def setup(dict):
    id = len(users)
    dict['id'] = id
    users.append(dict)

def getUserData(dict):
    covid_cnt = 0
    heart_attack_cnt = 0
    stroke_cnt = 0

    for symp in dict:
        if dict[symp] == 1:
            covid_cnt += CHECK_COVID(symp)
            heart_attack_cnt += CHECK_HEART_ATTACK(symp)
            stroke_cnt += CHECK_STROKE(symp)
    
    prop_covid = covid_cnt / COVID_SYMP_COUNT
    prop_strok = stroke_cnt / STROKE_SYMP_COUNT
    prop_heart_attack = heart_attack_cnt / HEART_ATTACK_SYMP_COUNT
