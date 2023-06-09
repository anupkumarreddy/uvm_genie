/*****************************************************************************************
   filename: uart_intf.sv
   author  : anup reddy
   description: This package contains uart interface
******************************************************************************************/

`ifndef __uart_intf__
   `define __uart_intf__

/*****************************************************************************************
   Interface decleration
******************************************************************************************/
interface uart_intf(input uart_clk, input uart_reset);

   logic uart_tx;
   logic uart_rx;
   logic uart_s1;
   logic uart_s2;

endinterface : uart_intf

`endif

/*****************************************************************************************
   End of file
******************************************************************************************/