def start_spring(**spring):
    spring_dict = {}
    result = ''
    for k, v in spring.items():
        if v not in spring_dict.keys():
            spring_dict[v] = []
        spring_dict[v].append(k)

    for k, v in sorted(spring_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f'{k}:\n'
        for el in sorted(v):
            result += f'-{el}\n'

    return result


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower", }
# print(start_spring(**example_objects))
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird", }
# print(start_spring(**example_objects))
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
