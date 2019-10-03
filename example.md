# Quadratic equations

An equation of the form $ax^2 + bx + c = 0$ is called a quadratic equation.

Let $D = b^2 - 4ac$. $D$ is known as the discriminant:

* When $D < 0$, a quadratic equation does not have real roots.
* When $D = 0$, a quadratic equations has a single root.
* When $D > 0$, a quadratic equations has 2 distinct roots.

The roots of a quadratic equation are given by:
\[ x = \frac{-b ± \sqrt{D}}{2a} \]

# Positive Semidefiniteness

Let $A$ be an $n$ by $n$ matrix over $\mathbb{R}$.
Then $A$ is said to be positive semidefinite iff
\[ \forall u \in \mathbb{R}^n, u^TAu \ge 0 \]

**Theorem**: A symmetric matrix is positive semidefinite
if all its eigenvalues are non-negative.

**Proof**:

Since [$A$ is real and symmetric, it is orthogonally diagonalizable](https://sharmaeklavya2.github.io/theoremdep/nodes/linear-algebra/eigenvectors/ortho-diag.html).

Let $v_1, v_2, \ldots, v_n$ be the orthonormal eigenvectors of $A$.
Let $\lambda_1 \ge \lambda_2 \ge \ldots \ge \lambda_n \ge 0$ be the corresponding eigenvalues.
Let $P$ be the matrix whose $i^{\textrm{th}}$ column is $v_i$.
Then $A = PDP^T$, where $D$ is a diagonal matrix whose $i^{\textrm{th}}$ entry is $\lambda_i$
and $P$ is an orthogonal matrix.

Let $v = P^Tu$.
\[ \|v\|^2 = (P^Tu)^T(P^Tu) = u^TPP^Tu = \|u\|^2 \]

\begin{align}
u^TAu &= u^T(PDP^T)u
\\ &= (P^Tu)^TD(P^Tu)
\\ &= \sum_{i=1}^n \lambda_i v_i^2
\\ &\ge \lambda_n \|v\|^2 \ge 0
\end{align}
