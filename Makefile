PYTHON = python3
SOURCE = cafe.py
TEST_MODULE = unittest
RM = rm -rf
ALL = testutil/*.py
CACHE = __pycache__/

all:	run
	@$(RM) testutil/$(CACHE)
	@$(RM) com/$(CACHE)
	@$(RM) com/kakao/$(CACHE)
	@$(RM) com/kakao/cafe/$(CACHE)
	@$(RM) com/kakao/cafe/menu/$(CACHE)
	@$(RM) com/kakao/cafe/menu/espresso/$(CACHE)
	@$(RM) com/kakao/cafe/menu/smoothie/$(CACHE)
	@$(RM) com/kakao/cafe/menu/tea/$(CACHE)
	@$(RM) com/kakao/cafe/menu/ade/$(CACHE)
	@$(RM) com/kakao/cafe/menu/dessert/$(CACHE)
	@$(RM) com/kakao/cafe/module/$(CACHE)

run:
	@echo "$$RYAN_ASCII"
	@$(PYTHON) $(SOURCE)

test:
	$(PYTHON) -m $(TEST_MODULE) $(ALL)
	@$(RM) testutil/$(CACHE)
	@$(RM) com/$(CACHE)
	@$(RM) com/kakao/$(CACHE)
	@$(RM) com/kakao/cafe/$(CACHE)
	@(RM) com/kakao/cafe/menu/$(CACHE)
	@(RM) com/kakao/cafe/menu/espresso/$(CACHE)
	@(RM) com/kakao/cafe/menu/smoothie/$(CACHE)
	@(RM) com/kakao/cafe/menu/tea/$(CACHE)
	@(RM) com/kakao/cafe/menu/ade/$(CACHE)
	@(RM) com/kakao/cafe/menu/dessert/$(CACHE)
	@(RM) com/kakao/cafe/module/$(CACHE)
	
cafemenu:
	$(PYTHON) -m $(TEST_MODULE) testutil/testCafeMenu.py
	@(RM) testutil/$(CACHE)
	@(RM) com/$(CACHE)
	@(RM) com/kakao/$(CACHE)
	@(RM) com/kakao/cafe/$(CACHE)
	@(RM) com/kakao/cafe/menu/$(CACHE)

espresso:
	$(PYTHON) -m $(TEST_MODULE) testutil/testEspresso.py
	@(RM) testutil/$(CACHE)
	@(RM) com/$(CACHE)
	@(RM) com/kakao/$(CACHE)
	@(RM) com/kakao/cafe/$(CACHE)
	@(RM) com/kakao/cafe/menu/$(CACHE)
	@(RM) com/kakao/cafe/menu/espresso/$(CACHE)

smoothie:
	$(PYTHON) -m $(TEST_MODULE) testutil/testSmoothie.py
	@(RM) testutil/$(CACHE)
	@(RM) com/$(CACHE)
	@(RM) com/kakao/$(CACHE)
	@(RM) com/kakao/cafe/$(CACHE)
	@(RM) com/kakao/cafe/menu/$(CACHE)
	@(RM) com/kakao/cafe/menu/smoothie/$(CACHE)

tea:
	$(PYTHON) -m $(TEST_MODULE) testutil/testTea.py
	@(RM) testutil/$(CACHE)
	@(RM) com/$(CACHE)
	@(RM) com/kakao/$(CACHE)
	@(RM) com/kakao/cafe/$(CACHE)
	@(RM) com/kakao/cafe/menu/$(CACHE)
	@(RM) com/kakao/cafe/menu/tea/$(CACHE)

ade:
	$(PYTHON) -m $(TEST_MODULE) testutil/testAde.py
	@(RM) testutil/$(CACHE)
	@(RM) com/$(CACHE)
	@(RM) com/kakao/$(CACHE)
	@(RM) com/kakao/cafe/$(CACHE)
	@(RM) com/kakao/cafe/menu/$(CACHE)
	@(RM) com/kakao/cafe/menu/ade/$(CACHE)

dessert:
	$(PYTHON) -m $(TEST_MODULE) testutil/testDessert.py
	@(RM) testutil/$(CACHE)
	@(RM) com/$(CACHE)
	@(RM) com/kakao/$(CACHE)
	@(RM) com/kakao/cafe/$(CACHE)
	@(RM) com/kakao/cafe/menu/$(CACHE)
	@(RM) com/kakao/cafe/menu/dessert/$(CACHE)

module:
	$(PYTHON) -m $(TEST_MODULE) testutil/testModule.py
	@(RM) testutil/$(CACHE)
	@(RM) com/$(CACHE)
	@(RM) com/kakao/$(CACHE)
	@(RM) com/kakao/cafe/$(CACHE)
	@(RM) com/kakao/cafe/module/$(CACHE)

clean:
	$(RM) testutil/$(CACHE)
	$(RM) com/$(CACHE)
	$(RM) com/kakao/$(CACHE)
	$(RM) com/kakao/cafe/$(CACHE)
	$(RM) com/kakao/cafe/menu/$(CACHE)
	$(RM) com/kakao/cafe/menu/espresso/$(CACHE)
	$(RM) com/kakao/cafe/menu/smoothie/$(CACHE)
	$(RM) com/kakao/cafe/menu/tea/$(CACHE)
	$(RM) com/kakao/cafe/menu/ade/$(CACHE)
	$(RM) com/kakao/cafe/menu/dessert/$(CACHE)
	$(RM) com/kakao/cafe/module/$(CACHE)

ascii:
	@echo "$$RYAN_ASCII"


define RYAN_ASCII

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKK000KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNWWMMMWKkxxxxkxxxONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0OkkkkOKXOdxO000000OdkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkxkOO00OkkxodO00000000Oxx0WMMMMMMMMMMMWWNXXKXXXNWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWNXK000OOOO0KXNWMMNkdO00000000OxdxO000000000kdkXWMMMMMMNKOkxxxxxxxxxkO0XWMMMMMMMMMMMM
MMMMMMMMMMMMWNKOkkkkOOOOOOkkkkO0NKxk00000000000OxxkO00000000OxdkKWMMN0xdxkOO0000OOOkxxdkKWMMMMMMMMMM
MMMMMMMMMMMN0kkO00000000000000Oxxxdx0000000000000OO00000000000OkxxOOxdkO0000000OOOOOOOOxdkXMMMMMMMMM
MMMMMMMMMMXkxO0000000000000OOkxxdxddk0000000000000000000000000000OxdodxkO00000O0OOOOOOOOkdxKWMMMMMMM
MMMMMMMMMNkxO00000000000OkxxxkkO00Oxdk000000000000000000000000000000OkxdddxkO000OOOOOOOOOkdxNMMMMMMM
MMMMMMMMW0xO00000000OkxxxkOO00000000kdxO00000000000000000000000000000000OkxdddxOO0OOOOOOOOddKMMMMMMM
MMMMMMMMNOx0000000OxxxkO0000000000000OxdxO0000000000000000000000000000000000OxdddkOOOOOOOOddKMMMMMMM
MMMMMMMMXkk0000OkxxkO000000000000000000OkO000000000000000000000000000000000000OOxddxOOOOOOdxXMMMMMMM
MMMMMMMMNOx00OkxxO000000000000000000000000000000000000000000000000000000000000000OkdoxkOOxd0WMMMMMMM
MMMMMMMMWKxkkxxO0000000000000000000000000000000000000000000000000000000000000000000OkdoxxxONMMMMMMMM
MMMMMMMMMNOdxO000000000000000000000000000000000000000000000000000000000000000000000OOOxookNMMMMMMMMM
MMMMMMMMW0xkO00000000000000000000000000000000000000000000000000000000000000000000000OOOkdd0WMMMMMMMM
MMMMMMMNOxk0000000000000000000000000000000000000000000000000000000000000000000000000OOOOOxdONMMMMMMM
MMMMMMNOxO00000000000000000000000000000000000000000000000000000000000000000000000000OOOOOOkdkNMMMMMM
MMMMMNOxO000000000000000000000000000000000000000000000000000000000000000000000000000OOOOOOOkdkNMMMMM
MMMMNOxO0000000000000000000000000000000000000000000000000000000000000000000000000000OOOOOOOOxdOWMMMM
MMMW0xk0000000000000000000000000000000000000000000000000000000000000OOOOOO0000000000OOOOOOOOOxd0WMMM
MMMXkkO000000000000000Oxddoooooooooodk00000000000000000000000dc::;;;;;;;;;;;oO00000OOOOOOOOOOkdxXMMM
MMW0xO0000000000000000o,.............:k000000000000000000000Oo,',,,,,,,,,,,,lO00000OOOOOOOOOOOxdOWMM
MMXkkO0000000000000000Odoodddddddddddk000000000000000000000000OOOOOOOOOOOOOO00000000OOOOOOOOOOkdxXMM
MMKxk000000000000000000000000000000000000000000000000000000000000000000000000000000OOOOOOOOOOOOxdKWM
MW0xO000000000000000000000000OOO000000000000000000000000000000000Oxoldk00000000000OOOOOOOOOOOOOxdOWM
MNOxO0000000000000000000000kl;,;oO0000000000000000000000000000000o'...;k0000000000OOOOOOOOOOOOOkdkWM
MNkxO0000000000000000000000o'...,x0000000000000000000000000000000o'...;k00000000000OOOOOOOOOOOOkdkNM
MNkxO0000000000000000000000Oo:;:oO00000000000000000000000000000000xolok0000000000000OOOOOOOOOOOkdkNM
MNOxO0000000000000000000000000O000000000000000kxddddkO00000000000000000000000000000OOOOOOOOOOOOkdkNM
MWOxO0000000000000OOOkkkkkOO000000000000kxdooc,.....';cllloxO000000000kxddddodddxkOOOOOOOOOOOOOkdOWM
MW0xk00000000000kxdooooooooodkO000000Odc:coooc.......;odddlc:lk00000Odlc:cccc:cccldOOOOOOOOOOOOxd0WM
MMXkkO000000000Odooooooolllllok00000k:;dKNNNNXx;...,o0NNNNNXk;;x0000koccccccccccccokOOOOOOOOOOOdxXMM
MMWOxO000000000OxoooooooollooxO0000Oc;kNNNNNNNNX0OOKNNNNNNNNNO,:O0000kdollllllloodkOOOOOOOOOOOkdkNMM
MMMXxxO000000000OOkkxxxxxxkkO000000O:;0NNNNNNNNNXKKXNNNNNNNNNO,:O000000OOOOOOOOOOOOOOOOOOOOOOOddKWMM
MMMW0xkO0000000000000000000000000000d,l0NNNNNNNKo,,lKNNNNNNN0c,d00000000000000OOOOOOOOOOOOOOOxdONMMM
MMMMNkxO00000000000000000000000000000x::lxkOkxo::cc::odxkxdl::x0000000000000000OOOOOOOOOOOOOkdxXMMMM
MMMMMXkxO00000000000000000000000000000OxolcccclxO00OxllcccloxO000000000000000000OOOOOOOOOOOkdxXMMMMM
MMMMMMXkxO000000000000000000000000000000000000000000000000000000000000000000000OOOOOOOOOOOkdxXWMMMMM
MMMMMMMXkxk0000000000000000000000000000000000000000000000000000000000000000000000OOOOOOOOkdkXWMMMMMM
MMMMMMMMN0xkO000000000000000000000000000000000000000000000000000000000000000000OOOOOOOOOxdONMMMMMMMM
MMMMMMMMMWXkxk0000000000000000000000000000000000000000000000000000000000000000OOOOOOOOxdxKWMMMMMMMMM
MMMMMMMMMMMN0kxO00000000000000000000000000000000000000000000000000000000000000OOOOOOxdx0NMMMMMMMMMMM
MMMMMMMMMMMMMN0kxkO0000000000000000000000000000000000000000000000000000000000OOOOOxdx0NWMMMMMMMMMMMM
MMMMMMMMMMMMMMMWKOkkO0000000000000000000000000000000000000000000000000000000OOOkxdk0NMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWX0OkkOO0000000000000000000000000000000000000000000000000OOkxxk0XWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWNKOOkkOO00000000000000000000000000000000000000000OOkxxxO0XWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWXKOOkkkkOO0000000000000000000000000000OOOkxxxkkO0XNWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX00OOkkkxkkkkkkOOOOOOOOOkkkkxxxxxxxkkO0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNXKK0OOOOkkkkkkkkkkkOOO00KXNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

endef
export RYAN_ASCII
