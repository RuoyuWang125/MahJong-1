from enum import Enum, unique


@unique
class MahJong(Enum):
    OneTong = 1
    TwoTong = 2
    ThreeTong = 3
    FourTong = 4
    FiveTong = 5
    SixTong = 6
    SevenTong = 7
    EightTong = 8
    NineTong = 9

    OneTiao = 11
    TwoTiao = 12
    ThreeTiao = 13
    FourTiao = 14
    FiveTiao = 15
    SixTiao = 16
    SevenTiao = 17
    EightTiao = 18
    NineTiao = 19

    OneWan = 21
    TwoWan = 22
    ThreeWan = 23
    FourWan = 24
    FiveWan = 25
    SixWan = 26
    SevenWan = 27
    EightWan = 28
    NineWan = 29

    DongFeng = 31
    NanFeng = 33
    XiFeng = 35
    BeiFeng = 37
    Zhong = 41
    Fa = 43
    Bai = 45
