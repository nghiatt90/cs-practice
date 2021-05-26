// https://app.codesignal.com/challenge/4ndGLkRyYiYK7gyAy
int i, j, k, c, l;
int Counting_Triangles(int[] V) {
  l = V.length;
  Arrays.sort(V);
  for (; i < l; ++i)
    for (j = i + 1; j < l; ++j)
      for (k = j + 1; k < l;)
    c += V[i] + V[j] > V[k++] ? 1 : 0;
    return c;
}

