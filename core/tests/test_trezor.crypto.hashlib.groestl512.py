# flake8: noqa: F403,F405
from common import *  # isort:skip

from trezor.crypto import hashlib


class TestCryptoGroestl512(unittest.TestCase):

    # vectors from www.groestl.info/Groestl.zip #/KAT_MCT/*
    vectors = [
        (
            b"",
            "6D3AD29D279110EEF3ADBD66DE2A0345A77BAEDE1557F5D099FCE0C03D6DC2BA8E6D4A6633DFBD66053C20FAA87D1A11F39A7FBE4A6C2F009801370308FC4AD8",
        ),
        (
            unhexlify("C1ECFDFC"),
            "4726D760203C1EAF847F6837C74C16ADCEF5B55EAD5768A7C13E21A33D0D7B740F52DE8C81356DA63DABA791DA6680AF015DEB81246550201F232822BB087CE5",
        ),
        (
            unhexlify("82E192E4043DDCD12ECF52969D0F807EED"),
            "8CD831960FE9726055F7B3693CC5639DB7D01EDDA045AE41E877853111C4CF53D26D5B4E135118571721C247ACA6607979A4DF73849D1477365F7DB0149FBC9F",
        ),
        (
            unhexlify(
                "F5961DFD2B1FFFFDA4FFBF30560C165BFEDAB8CE0BE525845DEB8DC61004B7DB38467205F5DCFB34A2ACFE96C0"
            ),
            "CE24486770D443B423274DD30AF746EA4080065393D13DF0535709E260CF14B033CCD190A9FA5F81705178EB656031A6F1465A5A993BE62BE8D43931950BD5DB",
        ),
        (
            unhexlify(
                "2B6DB7CED8665EBE9DEB080295218426BDAA7C6DA9ADD2088932CDFFBAA1C14129BCCDD70F369EFB149285858D2B1D155D14DE2FDB680A8B027284055182A0CAE275234CC9C92863C1B4AB66F304CF0621CD54565F5BFF461D3B461BD40DF28198E3732501B4860EADD503D26D6E69338F4E0456E9E9BAF3D827AE685FB1D817"
            ),
            "FF410B511135DBC0B8644C28EFA3EC632326FEB98E50EDC6390C441610D7C514ACDF0A61A0BF01AA9DC1F55D92E085248EBA1C24EE23978B4986AF41C13A6176",
        ),
        (
            unhexlify(
                "EECBB8FDFA4DA62170FD06727F697D81F83F601FF61E478105D3CB7502F2C89BF3E8F56EDD469D049807A38882A7EEFBC85FC9A950952E9FA84B8AFEBD3CE782D4DA598002827B1EB98882EA1F0A8F7AA9CE013A6E9BC462FB66C8D4A18DA21401E1B93356EB12F3725B6DB1684F2300A98B9A119E5D27FF704AFFB618E12708E77E6E5F34139A5A41131FD1D6336C272A8FC37080F041C71341BEE6AB550CB4A20A6DDB6A8E0299F2B14BC730C54B8B1C1C487B494BDCCFD3A53535AB2F231590BF2C4062FD2AD58F906A2D0D"
            ),
            "3AE2AABD659C5844C923FD171CA36431A7E606ECA52A21B96A0F5E8CD1FA24141BEDAADF58608781DFABC103FE929CD2EADE8D6FBD6185D4F4B855DCA610D7A0",
        ),
        (
            unhexlify(
                "724627916C50338643E6996F07877EAFD96BDF01DA7E991D4155B9BE1295EA7D21C9391F4C4A41C75F77E5D27389253393725F1427F57914B273AB862B9E31DABCE506E558720520D33352D119F699E784F9E548FF91BC35CA147042128709820D69A8287EA3257857615EB0321270E94B84F446942765CE882B191FAEE7E1C87E0F0BD4E0CD8A927703524B559B769CA4ECE1F6DBF313FDCF67C572EC4185C1A88E86EC11B6454B371980020F19633B6B95BD280E4FBCB0161E1A82470320CEC6ECFA25AC73D09F1536F286D3F9DACAFB2CD1D0CE72D64D197F5C7520B3CCB2FD74EB72664BA93853EF41EABF52F015DD591500D018DD162815CC993595B195"
            ),
            "F88E8E86FBE2200E90226A181E48348E06D1643270C079B8BDD3660E8D21CD0493C55051CBFA607B1CFACA2C5A2C9354CDD405C1D3AD1D8435B825884CC0559F",
        ),
        (
            unhexlify(
                "D0FF6E045F4B636F75A389799F314066644854821B6E7AE4047ADFDE2D0C0E02C250F0BE582BEC94011189B964A8AF430F5921ED9D9F4446E4C788515B89CA69E5F7CDFCCC9E83E8F9460145B43DDC41C07CC512B7E6FDD0E1E7AABA29A6C016CCB7BD54B145F3951EAB9BC4908F623E5A9B0C5B36056292540B79FD15C53457DC74A65FD773A34D6B313A056F79BC29A3FAC15F6A1446BFAEEAAFBAC8ECF8168DDE5F6AE6B6E579BD3CE74E7ABFADF361D0FD32D56586A8D2D4FF4CFDF8A750FAFDE4C2E9EB32B06847FA30B13CC273532D1A23C8257F80C60B8FA94FA976F534145CD61C41C0A511B62CADD5848CEFF643F83CE43F8E6969C5A559AFAD60E310599A34B2E5E029FBDDF2988FCE59269C7128A1FC79A74B154D8AA2850DCFDBF594684E74099E37882B440367C1DD3003F61CAFB46AC75D30E677AF54559A5DAB70C506CF61A9C35E0E56E1430746916DDEEC8D89B0C10DAA02C5D7E9F42621D2B312EAFFC9FF306297952A32D26C2148570AEC90501CA739CE5E689E7066D9580A4FC25E2023897C74C6856273133E1275A0D275DC5B75DB724CD12C9C01BB95AB5A227B7850020630506096878D289923177183EA9282A4C78EC212D2E898CB99D81A3364DF20927EE34D4475A5CF5CDB24088ED75B60201922E9C972D8556CA75F8274D15F3FB88A6B42C766DEF6B21329DEE7C457446DDE8C26405FE5D0309A04229F449E8490CF9000EE8DF400CB7C7EE831BD7059D24088FB42D61681CDE45050FCA78FF64D9C8D1F58B55F802FA5D2F2E723F3E4EED4338B060D31C8ACC46D26870BD45D0DE0798D48E32AAD1A6D4322E69F5E72309B9D7FA1F24BB1D63FF09ED47391C232497BF222C542A70975C8292D275197A4CA"
            ),
            "27AB9EA01D8FD80ED14990761ED6BC329DC842770F83FDD1CE95C0A074D6D7495C7C85297CC73F3A695377E4211F897F68C1A7F910F6BF440264FB63F120ABA2",
        ),
    ]

    def test_digest(self):
        for b, d in self.vectors:
            self.assertEqual(hashlib.groestl512(b).digest(), unhexlify(d))

    def test_update(self):
        for b, d in self.vectors:
            x = hashlib.groestl512()
            x.update(b)
            self.assertEqual(x.digest(), unhexlify(d))

        # Test from ExtremelyLongMsgKAT_512.txt, disabled by default because it resource-expensive
        # x = hashlib.groestl512()
        # for i in range(16777216):
        #     x.update(b'abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmno')
        # self.assertEqual(x.digest(), unhexlify('787C88460E5D09ABD7A98C050F3422BBFDBD36A74B05DE04B57A13FA3F36A570B8561580AB9DA4096CCD5111B5DE948F769D9D61833A6CE2B2F223061E688994'))

    def test_digest_multi(self):
        x = hashlib.groestl512()
        d0 = x.digest()
        d1 = x.digest()
        d2 = x.digest()
        self.assertEqual(d0, d1)
        self.assertEqual(d0, d2)


if __name__ == "__main__":
    unittest.main()
