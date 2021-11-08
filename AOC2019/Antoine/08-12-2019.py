def readFile():
    with open(__file__[:10] + "-" + "input.txt", "r") as f:
        return f.read()[:-1]

def getLayers(vals, wide, tall):
    layersSize = wide * tall
    layersList = []
    for i in range(len(vals)//layersSize):
        layersList.append(vals[i * layersSize: (i+1) * layersSize])
    return layersList

def stackingLayers(layersList, wide, tall):
    image = '\n'
    layersSize = wide * tall
    for pixel in range(layersSize):
        for layer in layersList:
            if layer[pixel] == '2':
                continue
            else:
                image += layer[pixel]
                if (pixel + 1) % 25 == 0:
                    image += '\n'
                break
    image = image.replace('0', ' ').replace('1', 'X')
    return image

def part1(vals):
    layersList = getLayers(vals, 6, 25)
    fewestZeroLayer = sorted(layersList, key=lambda layer: layer.count('0'))[0]
    return fewestZeroLayer.count('1') * fewestZeroLayer.count('2')

def part2(vals):
    layersList = getLayers(vals, 6, 25)
    image = stackingLayers(layersList, 6, 25)
    return image

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")

