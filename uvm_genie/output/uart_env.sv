/*****************************************************************************************
   filename: uart_env
   author  : anup reddy
   description: This package contains uart env
******************************************************************************************/
`ifndef __uart_env__
   `define __uart_env__

class uart_env extends uvm_env;
 `uvm_component_utils(`uart_env)

  function new(string name = "uart_env", uvm_component parent);
    super.new(name, parent);
  endfunction : new

  virtual void function build_phase(uvm_phase phase);
    super.build_phase(phase);
  endfunction : build_phase

  virtual void function connect_phase(uvm_phase phase);
    super.connect_phase(phase);
  endfunction : connect_phase


endclass : uart_env

`endif
/*****************************************************************************************
   End of file
******************************************************************************************/