import pandas as pd
import re 

import nltk
from nltk.corpus import wordnet

from dataExchange import Graph, Node, LeafNode, RootNode


# Téléchargement des ressources nécessaires
nltk.download('wordnet')
nltk.download('omw-1.4')


# Define the path to your .tsv file
file_path = "list-yago-types.tsv"

# Read the .tsv file into a DataFrame
df = pd.read_csv(file_path, sep="\t", header=None)

file_path_facts = "list-yago-facts.tsv"

# Read the .tsv file into a DataFrame
df_facts = pd.read_csv(file_path_facts, sep="\t", header=None)

file_path = "yago-taxonomy.tsv"

# Read the .tsv file into a DataFrame getting rid of the first 34 rows
taxonomy = pd.read_csv(file_path, sep="\t", header=None, skiprows=34)

concepts = []
with open('codes.csv', 'rt', encoding='utf-8') as codes:
    for line in codes:
        split=line.lower().split('\n')[0].split(',')[1:]
        concepts = concepts + split
concepts = set(concepts)


def get_main_label(word, df_yago):
    # replace the space by "_" in the word
    word = word.replace(" ", "_")
    # add yago: as a prefix
    word = "yago:" + word
    # check if the word is in the DataFrame df_yago in column 0
    if word in df_yago[0].values:
        # get the corresponding label in column 2
        label = df_yago[df_yago[0] == word][2].values[0]
        return [label]
    else:
        return None

def get_all_parents_from_main_label(labels, taxonomy):
    # check if the label is in the taxonomy DataFrame in column 0
    for label in labels:
        if label in taxonomy[0].values:
            # get the corresponding parent in column 0
            parents = list(taxonomy[taxonomy[0] == label][2])
            # add the parent to the list
            # recursive call to get all the parents of the parent
            parents += get_all_parents_from_main_label(parents, taxonomy)
            return parents
        else:
            return []

def get_all_relations(word, df_yago):
    # replace the space by "_" in the word
    word = word.replace(" ", "_")
    # add yago: as a prefix
    word = "yago:" + word
    # get all columns 2 where the word is in column 0
    if word in df_yago[0].values:
        return list(df_yago[df_yago[0] == word][2])
    else:
        return None

    
# Fonction pour trouver les dérivés d'un mot
def get_derived_words(word):
    derived_words = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            for deriv in lemma.derivationally_related_forms():
                derived_words.add(deriv.name())
    return derived_words

def get_synonyms(word):
    synonyms = set()  # Use a set to avoid duplicate synonyms
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return (synonyms)


def get_words_and_derived(main_labels, derived=False):
    all_main_labels = []
    for r in main_labels:
        if ":" in r:
            r =r.split(":")[1]
        rel = re.split(r' |_|__', r)
        rel = [r for r in rel if r.lower() in wordnet.words()]
        all_main_labels = all_main_labels + rel
        if derived:
            for w in rel:             
                all_main_labels = all_main_labels  + list(get_synonyms(w) & concepts | get_derived_words(w) & concepts)
    return all_main_labels

def word2id(word):
    with open('codes.csv', 'rt', encoding='utf-8') as codes:
        for line in codes:
            split=line.lower().split('\n')[0].split(',')
            for w in split[1:]:
                if word==w:
                    return int(split[0])
    return None


def get_graph(word_to_encode):
    main_labels = get_all_parents_from_main_label(get_main_label(word_to_encode, df), taxonomy)
    relations = get_all_relations(word_to_encode, df_facts)
    main_concept = set(get_words_and_derived(main_labels, False))
    leaf_nodes = set(get_words_and_derived(main_labels + relations, True)) & concepts
    main_concept = main_concept - leaf_nodes

    leaf_nodes = [LeafNode(cellID=word2id(concept)) for concept in leaf_nodes]
    nodes = [Node(comment=word) for word in main_concept ]
    all_nodes = leaf_nodes + nodes
    
    root_node = RootNode(txt=word_to_encode)
    
    for node in all_nodes:
        root_node.addChild(node)

    graph = Graph(nodes=all_nodes, root=root_node)
    
    return graph
