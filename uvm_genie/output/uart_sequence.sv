/*****************************************************************************************
   filename: uart_sequence.sv
   author  : anup reddy
   description: This package contains uart sequence
******************************************************************************************/

`ifndef __uart_sequence__
   `define __uart_sequence__

class uart_sequence extends uvm_sequence;

 `uvm_object_utils(uart_sequence)

  function new(string name = "uart_sequence");
    super.new(name);
  endfunction : new

  task body();
    start_item(item);
    finish_item(item);
    get_response(item);
  endtask : body

endclass : uart_sequence

`endif
/*****************************************************************************************
   End of file
******************************************************************************************/
