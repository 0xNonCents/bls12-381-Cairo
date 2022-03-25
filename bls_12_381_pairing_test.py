from utils.bls_12_381_pairing import pairing, cast_point_to_fq12, twist
from utils.bls_12_381_field import FQ, FQ2
from utils.bls_12_381_utils import cairo_bigint6


g1 = (
    FQ(3685416753713387016781088315183077757961620795782546409894578378688607592378376318836054947676345821548104185464507),  # noqa: E501
    FQ(1339506544944476473020471379941921221584933875938349620426543736416511423956333506472724655353366534992391756441569),  # noqa: E501
)

neg_g1 = (
    FQ(3685416753713387016781088315183077757961620795782546409894578378688607592378376318836054947676345821548104185464507),  # noqa: E501
    FQ(2662903010277190920397318445793982934971948944000658264905514399707520226534504357969962973775649129045502516118218),  # noqa: E501
)


g2 = (
    FQ2([
        352701069587466618187139116011060144890029952792775240219908644239793785735715026873347600343865175952761926303160,  # noqa: E501
        3059144344244213709971259814753781636986470325476647558659373206291635324768958432433509563104347017837885763365758,  # noqa: E501
    ]),
    FQ2([
        1985150602287291935568054521177171638300868978215655730859378665066344726373823718423869104263333984641494340347905,  # noqa: E501
        927553665492332455747201965776037880757740193453592970025027978793976877002675564980949289727957565575433344219582,  # noqa: E501
    ]),
)


def test():
    p1 = pairing(g2, g1)
    p2 = pairing(g2, neg_g1)

    print(p1.coeffs[0])
    print(p2.coeffs[0])

    print(p1 * p2)


def test_cast_g1_to_fq12():
    print(cast_point_to_fq12(g1))


def test_g2_twist():
    print(twist(g2))


if __name__ == '__main__':
    # test()
    # test_cast_g1_to_fq12()
    test_g2_twist()
