/*****************************************************************************************
   filename: uart_monitor.sv
   author  : anup reddy
   description: This package contains uart monitor
******************************************************************************************/
`ifndef __uart_monitor__
   `define __uart_monitor__

class uart_monitor extends uvm_monitor;
  virtual uart_intf m_vintf;

 `uvm_component_utils(uart_monitor)

  function new(string name = "uart_monitor", uvm_component parent);
    super.new(name, parent);
  endfunction : new

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
  endfunction : build_phase

  task run_phase(uvm_phase phase);
    // actual logic goes here.
  endtask : run_phase

endclass : uart_monitor

`endif
/*****************************************************************************************
   End of file
******************************************************************************************/