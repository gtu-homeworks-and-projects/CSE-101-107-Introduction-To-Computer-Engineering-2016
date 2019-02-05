"""Python is mainly an imperative language. But python is a high level language. It also gives us options to write our code in declaretive/functional ways. """

import csv
def get_user_input():
    kelime=str(input("\nWho: "))
    return kelime

def build_tree():
    tree = {"Sefayi":"Father",
"Hulya":"Mother",
"Aydanur":"Sister",
"Ali":"Uncle",
"Veli":"Uncle",
"Ayşe":"Aunt",
"Ahmet":"Grandfather",
"Ayşe2":"Grandmother",
"Onur":"Me"}
    print("List of Family Members:")
    for row in tree:
        print("  "+row)
    return tree

def main():
    family_tree=build_tree()
    word=get_user_input()
    if word in family_tree:
        y=family_tree[word]
        print(y+"\n")
    else:
        print("Not found\n")
main()
