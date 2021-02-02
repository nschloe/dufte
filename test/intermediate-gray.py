# github:
#   dark:
#     bg:    #0d1117
#     font:  #c9d1d9
#   light:
#     bg:    #ffffff
#     font:  #24292e
#
# stackoverflow:
#   dark:
#     bg:    #222526
#     font:  #dad7d2
#   light:
#     bg:    #ffffff
#     font:  #242729
#
# twitter:
#  default:
#     bg:
#     font:
#  dim:
#     bg:    #101921
#     font:  #e8e6e3
#
import colorio
import numpy as np


def hex_to_int(rgb):
    return tuple(int(rgb[i : i + 2], 16) for i in (0, 2, 4))


c = ["c9d1d9", "24292e"]
# c = ["dad7d2", "242729"]

srgb_linear = colorio.cs.SrgbLinear()

rgb_linear0 = srgb_linear.from_rgb255(hex_to_int(c[0]))
rgb_linear1 = srgb_linear.from_rgb255(hex_to_int(c[1]))

xyz0 = srgb_linear.to_xyz100(rgb_linear0)
xyz1 = srgb_linear.to_xyz100(rgb_linear1)

# cs = colorio.cs.CAM16UCS(0.69, 20, 4.074)
cs = colorio.cs.CIELAB()
# cs = colorio.cs.OKLAB()
cam0 = cs.from_xyz100(xyz0)
cam1 = cs.from_xyz100(xyz1)

# average
avg = (cam0 + cam1) / 2

# back to RGB
xyz = cs.to_xyz100(avg)
rgbl = srgb_linear.from_xyz100(xyz)
rgb255 = np.asarray(np.rint(srgb_linear.to_rgb255(rgbl)), dtype=int)

# back to hex
print("".join([hex(val)[2:] for val in rgb255]))
