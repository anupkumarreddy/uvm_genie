/*****************************************************************************************
   filename: uart_test
   author  : anup reddy
   description: This package contains uart test
******************************************************************************************/

`ifndef __uart_test__
   `define __uart_test__

class uart_test extends uvm_test;
 `uvm_component_utils(`uart_test)

  function new(string name = "uart_test", uvm_component parent);
    super.new(name, parent);
  endfunction : new

  virtual void function build_phase(uvm_phase phase);
    super.build_phase(phase);
  endfunction : build_phase

  virtual void function connect_phase(uvm_phase phase);
    super.connect_phase(phase);
  endfunction : connect_phase

  virtual task run_phase(uvm_phase phase);

  endtask : run_phase

  virtual task main_phase(uvm_phase phase);

  endtask : main_phase

endclass : uart_test

`endif
/*****************************************************************************************
   End of file
******************************************************************************************/