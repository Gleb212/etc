from lupa import LuaRuntime

lua = LuaRuntime(unpack_returned_tuples=True)
lua.eval('print(2)')