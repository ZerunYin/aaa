VCS_COMMON = vcs -full64 -sverilog -debug_access+all -timescale=1ns/1ps -ntb_opts uvm-1.2

TB_BASE_PACKAGE_NAME = {{tb_base_package_name}}/{{tb_base_package_name}}.sv

INCDIR_LIST =

IF_LIST = \
    cmd_pkg/cmd_if.sv \
    msg_pkg/msg_if.sv

PKG_LIST = \
    cmd_pkg/cmd_pkg.sv \
    msg_pkg/msg_pkg.sv

comp:
	$(VCS_COMMON) +incdir+$(INCDIR_LIST) $(IF_LIST) $(PKG_LIST)
