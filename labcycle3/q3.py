import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def show_bar(file):
    species = file["Species"]
    species_modified = species.drop_duplicates()
    species_frequency = species.value_counts()
    plt.bar(species_modified, species_frequency, width=0.4)
    plt.show()


def scatter_graph(file):
    file_pca = file.drop(columns=["Species"])
    pca = PCA(n_components=2)
    file_PCA = pca.fit_transform(file_pca)
    file_PCA = pd.DataFrame(file_PCA, columns=["pca1", "pca2"])
    colormap = plt.colormaps.get_cmap("jet")
    colors = file["Species"].astype("category").cat.codes
    file_PCA.plot.scatter(x="pca1",
                          y="pca2",
                          c=colors,
                          cmap=colormap)
    plt.xlabel("PCA1")
    plt.ylabel("PCA2")
    plt.show()


def hist_diagram(file):

    sepal_length = file['SepalLengthCm']
    sepal_width = file['SepalWidthCm']
    petal_length = file['PetalLengthCm']
    petal_width = file['PetalWidthCm']

    print("which histogram distribution to show")
    print("1 . sepal length")
    print("2 . sepal width")
    print("3 . petal length")
    print("4 . petal width")

    user_input = int(input("enter what to do : "))

    if user_input == 1:
        plt.hist(sepal_length, bins=10, color="red")
    elif user_input == 2:
        plt.hist(sepal_width, bins=10, color="red")
    elif user_input == 3:
        plt.hist(petal_length, bins=10, color="red")
    elif user_input == 4:
        plt.hist(petal_width, bins=10, color="red")

    plt.show()


file = pd.read_csv("Iris.csv")
running = True
while running == True:
    print(1, " show bar graph of species ")
    print(2, " show scattered graph of PCA ")
    print(3, " show historical diagram 1")
    print(4, "quit\n\n")
    input_user = input("what is your choice : ")
    input_user = int(input_user)
    print("")

    while input_user != 5:

        if input_user == 1:
            show_bar(file)
            break
        elif input_user == 2:
            scatter_graph(file)
            break
        elif input_user == 3:
            hist_diagram(file)
            break
        elif input_user == 4:
            running = False
            print("thank you")
            break
