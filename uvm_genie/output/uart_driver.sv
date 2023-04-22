/*****************************************************************************************
   filename: uart_driver.sv
   author  : anup reddy
   description: This package contains uart driver
******************************************************************************************/
`ifndef __uart_driver__
   `define __uart_driver__

class uart_driver extends uvm_driver;
  virtual uart_intf vintf;

 `uvm_component_utils(uart_driver)

  function new(string name = "uart_driver", uvm_component parent);
    super.new(name, parent);
  endfunction : new

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
  endfunction : build_phase

  task run_phase(uvm_phase phase);
    // actual logic goes here.
  endtask : run_phase

endclass : uart_driver

`endif
/*****************************************************************************************
   End of file
******************************************************************************************/
