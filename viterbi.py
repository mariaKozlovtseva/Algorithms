def viterbi(obs, states, start_pr, trans_pr, emiss_pr):
    V = [{}]
    path = {}
    # Initialize base cases (t == 0)
    for state in states:
        V[0][state] = start_pr[state] * emiss_pr[state][obs[0]]
        path[state] = [state]

    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
        # calculate conditional probs of each state given previous states
        # state0 - previous state
        for state in states:
            (probs, prev_state) = max((V[t-1][state0]*trans_pr[state0][state]*emiss_pr[state][obs[t]], state0) for state0 in states)
            V[t][state] = probs
            newpath[state] = path[prev_state] + [state]
        path = newpath
    # best last state and its probability
    last_prob, state = max((V[t][state], state) for state in states)
    probs = []
    for idx, prev_state in enumerate(path[state][:-1]):
        probs.append(V[idx][prev_state])
    probs.append(last_prob)

    return probs, path[state]

if __name__ == '__main__':
    states = ('Healthy', 'Fever')
    observations = ('normal', 'cold', 'dizzy')
    start_probability = {'Healthy': 0.6, 'Fever': 0.4}

    transition_probability = {
        'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
        'Fever': {'Healthy': 0.4, 'Fever': 0.6}
    }
    emission_probability = {
        'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
    }
    print(viterbi(observations, states, start_probability,
                  transition_probability, emission_probability))




