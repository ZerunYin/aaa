package {{package_name}};
  import uvm_pkg::*;
  import {{tb_package_name}}::*;

  `include "uvm_macros.svh"

  `include "{{agent_object_filename}}"
  `include "{{sequence_item_filename}}"
  `include "{{sequence_filename}}"
  `include "{{sequencer_filename}}"
  `include "{{driver_filename}}"
  `include "{{monitor_filename}}"
endpackage