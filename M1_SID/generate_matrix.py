import numpy as np

def generate_symetric_matrix(n):
    """
    Génère une matrice carrée symétrique bien conditionnée de taille n x n.
    """
    # Étape 1: Générer des valeurs propres positives distinctes
    eigenvalues = np.linspace(1, max(10,n//4), n)  # Par exemple, valeurs propres entre 1 et 10
    
    # Étape 2: Générer une matrice orthogonale aléatoire
    Q, _ = np.linalg.qr(np.random.randn(n, n))  # Décomposition QR pour obtenir Q
    
    # Étape 3: Construire la matrice symétrique bien conditionnée
    A = np.dot(Q, np.dot(np.diag(eigenvalues), Q.T))
    
    return A
