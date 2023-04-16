`ifndef {{TB_BASE_SEQUENCE_ITEM_FILENAME}}
`define {{TB_BASE_SEQUENCE_ITEM_FILENAME}}

class {{tb_base_sequence_item_name}} extends {{tb_base_sequence_item_basename}};
  `uvm_object_utils_begin({{tb_base_sequence_item_name}})
  `uvm_object_utils_end
  extern function new(string name = "{{tb_base_sequence_item_name}}");

endclass : {{tb_base_sequence_item_name}}


function {{tb_base_sequence_item_name}}::new(string name = "{{tb_base_sequence_item_name}}");
  super.new(name);
endfunction : new

`endif // {{TB_BASE_SEQUENCE_ITEM_FILENAME}}