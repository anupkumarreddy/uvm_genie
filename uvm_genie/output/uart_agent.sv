/*****************************************************************************************
   filename: uart_agent
   author  : anup reddy
   description: This package contains uart agent
******************************************************************************************/
`ifndef __uart_agent__
   `define __uart_agent__

class uart_agent extends uvm_agent;
 `uvm_component_utils(`uart_agent)

  function new(string name = "uart_agent", uvm_component parent);
    super.new(name, parent);
  endfunction : new

  virtual void function build_phase(uvm_phase phase);
    super.build_phase(phase);
  endfunction : build_phase

  virtual void function connect_phase(uvm_phase phase);
    super.connect_phase(phase);
  endfunction : connect_phase


endclass : uart_agent

`endif
/*****************************************************************************************
   End of file
******************************************************************************************/