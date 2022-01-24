class Solution(object):
    def printPyramid(self, layer: int):
        if layer > 0:
            ground_length = 2 * layer - 1

            for layer_idx in range(1, layer + 1):
                star_cnt = layer_idx * 2 - 1
                side_space_cnt = (ground_length - star_cnt) // 2

                star_str = "*" * star_cnt
                side_space_str = " " * side_space_cnt
                print(f"{side_space_str}{star_str}{side_space_str}")


if __name__ == "__main__":
    obj = Solution()

    ### Example ###

    for layer in range(0, 7):
        print(f"Layer = {layer}")
        obj.printPyramid(layer)
        print("")
