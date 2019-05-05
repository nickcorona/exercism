def find_anagrams(word, candidates):
    word_lower = word.lower()
    word_sorted = "".join(sorted(word_lower))

    # remove redundant words
    for candidate in candidates[:]:
        if word_lower == candidate.lower():
            candidates.remove(candidate)

    # sort candidate words
    candidates_sorted = []
    for candidate in candidates:
        candidates_sorted.append("".join(sorted(candidate.lower())))

    # check if word is in sorted candidates
    # if so return
    return_candidates = []
    for index, candidate in enumerate(candidates_sorted):
        if candidate == word_sorted:
            return_candidates.append(candidates[index])
    return return_candidates
