def align_seqs(seq1, seq2, score_mat):

    len1, len2 = len(seq1), len(seq2)
    dp_matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Filling up the matrix with scores
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            scores = [
                dp_matrix[i-1][j-1] + score_mat[seq1[i-1]][seq2[j-1]], # Match/Mismatch
                dp_matrix[i-1][j] + score_mat[seq1[i-1]]['-'],         # Deletion
                dp_matrix[i][j-1] + score_mat['-'][seq2[j-1]]          # Insertion
            ]
            dp_matrix[i][j] = max(scores)

    # Backtrack to find the alignment
    aligned_seq1, aligned_seq2 = '', ''
    i, j = len1, len2
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp_matrix[i][j] == dp_matrix[i-1][j-1] + score_mat[seq1[i-1]][seq2[j-1]]:
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            i, j = i - 1, j - 1
        elif i > 0 and dp_matrix[i][j] == dp_matrix[i-1][j] + score_mat[seq1[i-1]]['-']:
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            j -= 1

    return aligned_seq1, aligned_seq2, dp_matrix[len1][len2]

# Scoring matrix
scoring_matrix = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': 0}
}
x, y = "ATGCC", "TACGCA"

# Get the aligned sequences
result = align_seqs(x, y, scoring_matrix)
print(result)

# Result:
# ('-ATGCC-', 'TACG-CA', 0.9)