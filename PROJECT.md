# 1. INTRODUCTION

## Role Assignments

| Name | Role |
|------|------|
|   Àlex Ruiz   | Design     |
|   Marçal Garreta   | CFD     |
|   Guillem Carreta   | Experimentation     |

## Specifications of the axial fan of the project

The axial fan specifications have been established based on the project requirements and the characteristics of comparable industrial axial fans available on the market. These parameters define the main operating limits of the fan and will serve as a reference for the design process, CFD simulations, and experimentation.

- Diameter: 630 mm
- Maximum Rotational Speed: 1400 rpm  
- Maximum Airflow Rate: 17000 m³/h
- Estimated Power Consumption: 1700 W

## Group regulations

### 1. Communication & Meetings
* **Primary Channels:** WhatsApp for urgent matters and daily communication; GitHub for version control and code/CFD script repository.
* **Weekly Sync:** Meetings will take place every weekend, depenending on the availability of group members.

### 2. Workflow & Deliverables
* **Deadlines:** Individual tasks assigned to each role (Design, CFD, Experimentation) must be completed at least **24 hours before** the main submission deadline to allow peer review.
* **Repository Management:** All CAD models, mesh files, CFD scripts, and test logs must be regularly committed to the official team GitHub repository.

### 3. Decision Making & Quality Standards
* **Consensus:** Technical decisions (e.g., selecting blade profile, mesh refine criteria) will be made by consensus. In case of disagreement, a majority vote will decide.
* **Role Accountability:** Each member is responsible for the technical accuracy of their assigned area (Àlex: CAD/Design, Marçal: CFD Simulations, Guillem: Experimental Setup).

## Applications of our design

Industrial axial extraction fans are commonly used in warehouses, manufacturing facilities, workshops, and other large industrial spaces where high volumes of air need to be extracted.

The proposed fan is designed for an industrial warehouse, and is intended to remove hot, humid, contaminated, or stagnant air and improve overall ventilation.

The fan performance will be evaluated through theoretical calculations, CFD simulations, and experimental testing, focusing on airflow, pressure rise, power consumption, and aerodynamic efficiency.


## Industrial Axial Fan Examples

### Soler & Palau - HCFB/4-630/H

- Wall-mounted axial fan with fiberglass reinforced plastic propeller
- Single-Phase (HCFB) motor, 4 poles, IP65, F class (operating temperatures between -40ºC and +70ºC), thermal protection incorporated.

#### Technical Specifications:

Diameter: 630 mm  
Blades:   
Weight: 25 kg  
Motor Power: 1573 W  
Max. Speed: 1380 rpm  
Max. Flow Rate: 17230 m³/h   

### Sodeca - HC-71-6T/H IE3

- Wall-mounted axial fan with fiberglass reinforced plastic propeller with IP55 engine. (HC-71-6T/H IE3)
- Three-Phase motor
- High flow
- Technical data sheet: "https://d7rh5s3nxmpy4.cloudfront.net/CMP2671/files/1/SE07_HC_2019ES.pdf"


#### Technical Specifications:

Diameter:  0.71 m  
Blades:  10 blades 
Weight: 39 Kg  
Motor Power: 750 W  
Max. Speed: 940 RPM  
Max. Flow Rate: 17300 m**3/h  

### Systemair AW 630D4-2

- Wall-mounted axial fan with a square mounting plate and an aerodynamically designed impeller made of die-cast aluminium.
- Three-phase external rotor motor, four poles, IP54 protection and Class F insulation. The motor includes thermal contacts to prevent overheating and supports speed control.
<!-- https://www.systemair.com/en-rs/products/fans/axial-fans/aw -->
<!-- https://planetaklimata.com.ua/instr/Systemair/Systemair_Fans_AW_Data_sheet_Eng.pdf -->

#### Technical Specifications

Diameter: 630 mm  
Blades: 7
Weight: 32 kg  
Motor Power: 1900 W  
Max. Speed: 1340 rpm  
Max. Flow Rate: 17800 m³/h

# 2. Data of Selected Fan

## Thecnical specification of the projects (Selected fan)
### Soler & Palau - HCFB/4-630/H

- Wall-mounted axial fan with fiberglass reinforced plastic propeller
- Single-Phase (HCFB) motor, 4 poles, IP65, F class (operating temperatures between -40ºC and +70ºC), thermal protection incorporated.

#### Technical Specifications:

Diameter: 630 mm  
Blades: 7 blades   
Weight: 25 kg  
Motor Power: 1573 W  
Max. Speed: 1380 rpm  
Max. Flow Rate: 17230 m³/h

# 3. DESIGN

# 4. CFD

# 5. Experimentation
The objective of this secction is to design, size, and validate a standardized aerodynamic test bench for the experimental characterization of a commercial wall-mounted axial fan, in full compliance with **UNE-EN ISO 5801:2019** [1].

In turbomachinery testing, the measured performance curve of an axial fan depends heavily on the upstream and downstream flow boundary conditions (inlet swirl, velocity profile distortion, and back-pressure recovery). Consequently, **ISO 5801:2019** defines four standardized installation categories (Categories A, B, C, and D) to guarantee reproducible laboratory measurements [1]. Because our selected fan is an un-ducted plate-mounted axial fan designed to draw air from an open space and discharge directly into the atmosphere, it corresponds to **Installation Category A (Free Inlet, Free Outlet)** [1, 2].

![SO 5801 Fan Category](<images/Figure 1 - Fan Installation Categories.png>)

### Experimental Overview

| Test Specimen & Operating Point | Test Bench & Metrology Setup |
| :--- | :--- |
| **Fan Model:** Soler & Palau HCFB/4-630/H | **Standard:** UNE-EN ISO 5801:2019 (Category A, Clause 9.4) |
| **Impeller Diameter ($D_1$):** $0.630\ \mathrm{m}$ | **Flowmeter:** Multi-nozzle bulkhead ($2\times\varnothing 315$, $\varnothing 224$, $\varnothing 160\ \mathrm{mm}$) |
| **Nominal Speed ($N_0$):** $1380\ \mathrm{rpm}$ | **Shaft Power:** Inline rotary torque sensor ($0\text{–}20\ \mathrm{N\cdot m}$) |
| **Max Flow Rate ($q_{V,\max}$):** $4.79\ \mathrm{m^3/s}$ | **ISO Table 13 Limits ($k=2$):** $q_V \le 2.0\%$ \| $p_f \le 1.4\%$ \| $P_a \le 2.0\%$ \| $\eta_t \le 2.8\%$ |

---

## 5.1 Governing Variables and Mathematical Formulation

Characterizing the steady-state aerodynamic and mechanical performance of the axial fan requires coupling ambient thermodynamic state measurements with pneumatic pressure differentials and direct impeller shaft mechanics.

### A. Master Variable Matrix

| Domain | Quantity | Symbol | Unit | Acquisition Method / Governing Relation |
| :--- | :--- | :---: | :---: | :--- |
| **Ambient State** | Barometric pressure | $p_a$ | $\mathrm{Pa}$ | Direct absolute pressure measurement in laboratory |
| **Ambient State** | Dry-bulb temperature | $T_a$ | $\mathrm{^\circ C}$ | Direct RTD measurement upstream of intake ($\Theta_a = T_a + 273.15\ \mathrm{K}$) |
| **Ambient State** | Relative humidity | $h_{\mathrm{rel}}$ | $-$ | Direct capacitive hygrometer reading ($p_v = h_{\mathrm{rel}}\,p_{\mathrm{sat}}(T_a)$) |
| **Fluid Properties** | Humid air density | $\rho$ | $\mathrm{kg/m^3}$ | Derived from $(p_a, T_a, h_{\mathrm{rel}})$ via ISO 5801 Eqs. (25)–(26) |
| **Fluid Properties** | Dynamic viscosity | $\mu$ | $\mathrm{Pa\cdot s}$ | Linear ISO 5801 correlation: $\mu(T_a) = (17.1 + 0.048\,T_a)\times 10^{-6}$ |
| **Aerodynamics** | Mass & volumetric flow | $q_m,\ q_V$ | $\mathrm{kg/s},\ \mathrm{m^3/s}$ | Multi-nozzle differential pressure $\Delta p$; $q_V = q_m / \rho_1$ |
| **Aerodynamics** | Chamber gauge static pressure | $p_{e3}$ | $\mathrm{Pa}$ | 4-tap piezometric ring depression at $0.5\,D_1$ upstream ($p_{e3} = p_{s3} - p_a < 0$) |
| **Aerodynamics** | Fan static & total pressure | $p_{fs},\ p_f$ | $\mathrm{Pa}$ | $p_{fs} \approx -p_{e3}$; $\quad p_f = p_{fs} + p_{d1}$ where $p_{d1} = \frac{1}{2}\rho_1 (q_V/A_1)^2$ |
| **Shaft Mechanics** | Rotational speed & torque | $N,\ M$ | $\mathrm{rpm},\ \mathrm{N\cdot m}$ | Optical encoder ($n = N/60$, $\omega = 2\pi n$) and inline rotary strain-gauge transducer |
| **Shaft Mechanics** | Impeller shaft power | $P_a$ | $\mathrm{W}$ | Direct mechanical input: $P_a = M \cdot \omega = \frac{2\pi N M}{60}$ |
| **Performance** | Total & static efficiency | $\eta_t,\ \eta_s$ | $-$ | $\eta_t = \dfrac{q_V \, p_f}{P_a}$, $\qquad \eta_s = \dfrac{q_V \, p_{fs}}{P_a}$ |

### B. Thermodynamic Air Density & Dimensionless Similarity Laws

1. **Humid Air State Reduction (ISO 5801 Clause 12.2):**  
   Because air density shifts with laboratory weather conditions, local density $\rho$ is computed continuously from the humid-air gas constant $R_w$ ($R_d = 287.05\ \mathrm{J/(kg\cdot K)}$, $R_v = 461.50\ \mathrm{J/(kg\cdot K)}$):
   $$R_w = \frac{R_d}{1 - \dfrac{p_v}{p_a}\left(1 - \dfrac{R_d}{R_v}\right)}, \qquad \rho = \frac{p_a}{R_w \, \Theta_a}$$

2. **Buckingham $\Pi$ Dimensionless Coefficients (ISO 5801 Clause 15):**  
   Normalizing volumetric flow, pressure rise, and shaft power by the rotor reference area ($A_1 = \frac{\pi}{4}D_1^2 = 0.3117\ \mathrm{m^2}$) and blade tip speed ($u_{\mathrm{tip}} = \pi n D_1$) yields the invariant machine characteristics:
   $$\varphi = \frac{q_V}{A_1 \, u_{\mathrm{tip}}}, \qquad \psi_t = \frac{p_f}{\frac{1}{2}\rho_1 u_{\mathrm{tip}}^2}, \qquad \psi_s = \frac{p_{fs}}{\frac{1}{2}\rho_1 u_{\mathrm{tip}}^2}, \qquad \lambda = \frac{P_a}{\frac{1}{2}\rho_1 A_1 u_{\mathrm{tip}}^3}$$
   At nominal speed ($N_0 = 1380\ \mathrm{rpm}$), the machine Reynolds number is $\mathrm{Re}_D = \frac{\rho u_{\mathrm{tip}} D_1}{\mu} \approx 1.88 \times 10^6 \gg 10^5$, confirming self-similar turbulent operation.

## 5.2 Proposed Instrumentation for Measurement and Data Acquisition

The measurement chain follows the standard metrological sequence: physical sensor $\rightarrow$ analogue signal conditioning $\rightarrow$ simultaneous-sampling data acquisition (DAQ) chassis $\rightarrow$ numerical post-processing and GUM uncertainty propagation (Figure 1).

```text
Physical sensor  →  Analogue / TTL transducer  →  DAQ chassis (NI cDAQ-9174)       →  Post-processing
                    (0–10 V / RTD / TTL)          (NI-9205, NI-9217, NI-9401)         (Python / GUM)