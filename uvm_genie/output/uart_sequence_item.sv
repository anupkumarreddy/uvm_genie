/*****************************************************************************************
   filename: uart_sequence_item.sv
   author  : anup reddy
   description: This package contains uart sequence item
******************************************************************************************/

`ifndef __uart_sequence_item__
   `define __uart_sequence_item__

class uart_sequence_item extends uvm_sequence_item;

 `uvm_object_utils(uart_sequence_item)

  function new(string name = "uart_sequence_item");
    super.new(name);
  endfunction : new

endclass : uart_sequence_item

`endif
/*****************************************************************************************
   End of file
******************************************************************************************/
