## Projects:
**Pacemaker project:** A simulink pacemaker with accompanying python-based GUI
[<img align="right" alt="Python" width="22px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" />][python-org] [<img align="right" alt="Simulink" width="22px" src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" />][simulink]
  - Features multiple users support, serial communication, real-time plotting of pacemaker data. GUI can program and read pacemaker parameters over serial. APIs used include threading, pyserial, tkinter, matplotlib, and struct.

**ASIP Stepper motor controller:** Verilog FPGA stepper motor controller
[<img align="right" alt="Verilog" width="22px" src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_verilog_icon_130092.png" />][verilog] [<img align="right" alt="Quartus Prime" width="22px" src="https://www.jackenhack.com/wp-content/uploads/2020/01/Quartus_prime_icon.png" />][quartus]
  - Designed an ASIP using Verilog, including a 14-module datapath and control FSM on a Cyclone V FPGA to control a stepper motor
  - Constructed a motor driver interface circuit using an SN754410 Half-H Driver chip
  - Utilized Quartus Prime for simulation and testing of the ASIP and its modules. Additionally, wrote test programs in assembly to be run on ASIP.

**SDRAM Controller:** Verilog SDRAM controller
[<img align="right" alt="Verilog" width="22px" src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_verilog_icon_130092.png" />][verilog] [<img align="right" alt="Quartus Prime" width="22px" src="https://www.jackenhack.com/wp-content/uploads/2020/01/Quartus_prime_icon.png" />][quartus]
  - Designed a controller circuit for an SDRAM chip on a Cyclone V FPGA
  - Controller is able to read and write data to the DRAM

**Subcontractor Scraper:** A project I worked on during my time as a project coordinator at a construction company
[<img align="right" alt="Python" width="22px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" />][python-org] [<img align="right" alt="VBA" width="89px" src="https://user-images.githubusercontent.com/93336604/152653144-b4f6eee1-0cf8-4ef3-a551-8e4ce8705c89.png" />][vba]
  - Taking in a list of desired subcontractors from a word document, it searches the company's excel sheet for the subcontractor's contact information
  - Once acquired, it sorts the information by subtrade then inserts it into a macro-enabled excel document, which I programmed using VBA
  - The time required to manually fill this excel document was incredibly long, which inspired me to create this application in order to speed up the process

**InsiderBot:** A personal project that I created when I began trading in the stock market
[<img align="right" alt="Python" width="22px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" />][python-org]
  - Uses Discord for input and output
  - Reports information on a specified stock (50 day average, daily high, daily low, yield, etc)
  - Provides insider trades information: CEOs/company heads/politicians that bought or sold large amounts of company stock
  - Uses requests and beautifulsoup python libraries to scrape the web for the above information, as well as the discord library

**PWM Fan Controller:** A project for my embedded systems design class, MECHTRON 2TA4
[<img align="right" alt="C" width="22px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/C_Programming_Language.svg/695px-C_Programming_Language.svg.png" />][c-prog]
  - Created a heat-activated PWM fan device using a temperature sensor, operational amplifier, and an opto-isolator in conjunction with an STM32 MCU.
  - Implemented a variety of functions in embedded C, such as display of the current temperature on an LCD, a user-modifiable threshold temperature, and PWM fan 
    operation based on temperature.

**Tic-Tac-Toe:** A basic JavaScript-HTML-CSS project
[<img align="right" alt="C" width="22px" src="https://www.mycplus.com/mycplus/wp-content/uploads/2008/09/JavaScript.png" />][js][<img align="right" alt="C" width="24px" src="https://www.w3.org/html/logo/downloads/HTML5_Badge_512.png" />][html][<img align="right" alt="C" width="22px" src="https://camo.githubusercontent.com/119b29ca4b9d31cf3969a94eb57fcfbbea0879b493c09c89dc6d4b7fb9e0dc37/68747470733a2f2f63646e2e776f726c64766563746f726c6f676f2e636f6d2f6c6f676f732f6373732d332e737667" />][css]
  - Created a simple game of Tic-Tac-Toe with plans to add more games in the future

**3D-Printable Lightsaber:**
[<img align="right" alt="C" width="88px" src="https://yourengineer.in/wp-content/uploads/2021/07/autodesk-inventor-logo.png" />][fusion][<img align="right" alt="C" width="88px" src="https://i.pinimg.com/originals/f5/6b/60/f56b60f21d1afcdd41278048afcc75bf.png" />][inventor]
  - Used Inventor and Fusion360 to design, prototype, and model a to-scale 3D model of a lightsaber handle from Star Wars. 
  - Original design was restructured into an assembly to allow for 3D printing.

[linkedin]: https://www.linkedin.com/in/alexander-bartella-02/
[python-org]: https://www.python.org/
[c-prog]: https://devdocs.io/c/
[cpp]: https://docs.microsoft.com/en-us/cpp/?view=msvc-170
[keil-Arm]: https://www.keil.com/support/man/docs/armasm/armasm_dom1359731145130.htm
[vba]: https://docs.microsoft.com/en-us/office/vba/api/overview/
[vscode]: https://code.visualstudio.com/
[git-scm]: https://git-scm.com/
[ubuntu]: https://ubuntu.com/
[js]: https://javascript.com/
[html]: https://www.w3.org/standards/webdesign/htmlcss
[css]: https://www.w3.org/Style/CSS/Overview.en.html/
[fusion]: https://www.autodesk.ca/en/products/fusion-360/
[inventor]: https://www.autodesk.ca/en/products/inventor/
[simulink]: https://www.mathworks.com/products/simulink.html
[quartus]: https://www.intel.ca/content/www/ca/en/products/details/fpga/development-tools/quartus-prime.html
[verilog]: https://verilogguide.readthedocs.io/en/latest/
