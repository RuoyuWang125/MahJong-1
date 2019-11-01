import time

import MahJong


class MahJongCalculate:
    def __init__(self, hand_cards):
        self.__hand_cards = hand_cards

    def calculate_hu(self):
        """
        计算
        :return:
        """
        _double = []
        for x in self.__hand_cards:
            if self.__hand_cards.count(x) >= 2:
                _double.append(x)
        if len(_double) == 0:
            return False
        for d in _double:
            _hand_cards = self.__hand_cards.copy()
            _hand_cards.sort()
            _hand_cards.remove(d)
            _hand_cards.remove(d)
            _hand_tong = [x for x in _hand_cards if x < MahJong.MahJong.OneTiao.value]
            _hand_tiao = [x for x in _hand_cards if MahJong.MahJong.OneWan.value > x > MahJong.MahJong.NineTong.value]
            _hand_wan = [x for x in _hand_cards if MahJong.MahJong.NineTiao.value < x < MahJong.MahJong.DongFeng.value]
            _hand_feng = [x for x in _hand_cards if x > MahJong.MahJong.NineWan.value]
            _hand = [_hand_tong, _hand_tiao, _hand_wan, _hand_feng]
            for _h in _hand:
                for index, value in enumerate(_h):
                    if index % 3 != 0:
                        continue
                    if _h[index+1] != _h[index+2] != value and (
                            _h[index + 2] - value != 2 and _h[index + 1] - value != 1):
                        return False
            return True


_h = [MahJong.MahJong.OneWan.value, MahJong.MahJong.OneWan.value,
      MahJong.MahJong.TwoWan.value, MahJong.MahJong.ThreeWan.value,  MahJong.MahJong.FiveWan.value,
      MahJong.MahJong.OneTiao.value, MahJong.MahJong.TwoTiao.value, MahJong.MahJong.ThreeTiao.value,
      MahJong.MahJong.FiveTiao.value, MahJong.MahJong.SixTiao.value, MahJong.MahJong.SevenTiao.value,
      MahJong.MahJong.OneTong.value, MahJong.MahJong.TwoTong.value, MahJong.MahJong.ThreeTong.value
      ]
m = MahJongCalculate(_h)
print(m.calculate_hu())
