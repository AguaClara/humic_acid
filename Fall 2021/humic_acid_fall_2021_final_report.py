# -*- coding: utf-8 -*-
"""Humic Acid Fall 2021 Final Report.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gxRjrZHg2fpFZIz1aoeFkFnxCIio37lh

# **Humic Acid, Fall 2021**
#### Lynn Shin, Rachel Lai, Annie Hsu, and Dennis Wu
#### December 7th, 2021

## **Abstract**
The Fall 2021 Humic Acid Removal subteam is centered around setting up the lab to be able to run preliminary experiments. One of our goals in the lab to validate the relationship between coagulant dosage and humic acid concentration in order to effectively remove the humic acid from the water in substandard conditions. The team will also be working towards defining a steady state, which has not yet been determined by the subteam in previous years. Thus, more reliable and contributive data can be obtained to make it easier to redesign our experiment more accurately. Another goal is to design an automated ProCoDa code that would allow experiments to run for longer periods of time without having pauses in the experiments.

## **Introduction**
The subteam’s goal is to develop methods to remove harmful dissolved Natural Organic Matter (NOM), specifically humic acid, from influent water in an AguaClara plant.

NOM exists in both ground and surface water. It is dipolar and can serve as a nutrient for bacteria, viruses, and pathogens. Additionally, some NOM produces carcinogenic byproducts during chlorination.The subteam will be using humic acid (HA) as a representative substance for NOM.  Humic acid reacts with chlorine to form chloroform, which is harmful to humans (Kopfler, F et al.). To minimize risk, it is imperative to remove NOM from water. However, there is not a robust model predicting how NOM behaves in water. Consequently, there are no effective treatment methods for NOM-water removal. Limited knowledge in this area affects drinking water treatment significantly. Many researchers believe the negative effects of NOM in water might call for a need to increase coagulant doses. The cost of coagulant and its potential negative effects in excess set a maximum limit for the dose that can be added during the water treatment process. One such negative effect is that too much coagulant prevents flocculation.

At the AguaClara plant in Gracias, Honduras, influent water contains an unusually high concentration of dissolved NOM (specifically HA) while containing relatively little clay. This composition has presented issues. Generally, suspended clay particles in influent water serve as catalysts for flocs to form, allowing NOM to coagulate and leave solution. With little clay in the influent water, floc formation is slower and less probable, making it difficult to encourage flocculation of dissolved NOM. In the past, this sub-team's goal was to determine whether increasing the dosage of coagulant (specifically PACl) would facilitate better flocculation of NOM. In the Fall 2019 semester, this subteam demonstrated that it is possible to use PACl to encourage flocculation of dissolved HA and determined a few potentially optimal PACl dosages to do so.

For the Fall 2021 semester, the subteam aims to retest the optimal PACl dosages for humic acid removal that were determined by past team members. The subteam hopes to make meaningful progress towards developing a reliable method for HA removal, and towards applying this method to the general removal of NOM.

## **Literature Review**
Natural organic matter (NOM) can pose dangers to water quality. It causes discoloration, taste and odor problems, and biological growth in distribution systems. It’s presence increases the probability of heavy metal intoxication in freshwater systems, which poses a threat to communities relying on said bodies of water. There is a strong positive association between high amounts of natural organic matter and high sludge volumes post-water treatment.  Matilainen et al.(2010) suggests that optimized coagulation is the major treatment option in decreasing NOM level. However, the nature of NOM has significant effects on the removal efficiency of coagulation. NOM particle removal is affected by several factors such as pH and temperature. In this case, a lower than average pH affects the electrical charge for humic acid particles, which could affect their interactivity with the coagulant used.

As suggested by Zhang et al. (2008), polyaluminium chloride presents a viable coagulant to combat NOM (specifically humic acid) contamination in bodies of water. Usual aluminium coagulants are usually efficient, but PaCl has demonstrated to have higher efficiency despite its low cost. Zhang et al. (2008) also warns that overuse of PaCl to treat water could lead to a contamination of aluminium in the bodies of water, which would then lead it to require additional treatment.

As shown with the studies conducted by Soh et al. (2008), NOMs (such as humic acid) can be subdivided into different categories based on their hydrophobic or hydrophilic properties (very hydrophobic acids, slightly hydrophobic acids, charged hydrophilics, and neutral hydrophilics). During this study, it was supported that aluminium coagulation would not suffice for all types of NOM particle removal treatment, as some of the NOMs were not interacting with it. This directly ties with what Zhang et al. (2008) argued in favor of the use of PaCl as a much more viable alternative. Soh’s study also suggests that common water treatments have not shown to improve in effectiveness with increased dosage quantities, which further supports the use of PaCl over aluminium as coagulant.

Research has been done by Yingda Du, former Cornell University student, on how effluent turbidity is affected by a combination of coagulant concentration and concentration of humic acid. Amongst the relevant discoveries of Du’s research, lies the fact that particle distribution of flocs and effluent turbidity are the major criteria that determines flocculation effectiveness. These factors, in turn, are directly affected by NOM (in this case humic acid) concentration.  Du’s research showed that for influent turbidity at 50 NTU with coagulant dosage ranging from 0.53 mg/L to 2.65 mg/L and humic acid concentration ranging from 0 to 15 mg/L, a series of experiments from Yingda indicate that the coagulant dosage is positively correlated with turbidity reduction and the presence of humic acid greatly increases the effluent turbidity


Another finding from Du's report is that the presence of humic acid increases the frequency of smaller particles after flocculation. As humic acid coats coagulant nano-particles, the attachment efficiency of collisions will decrease. Thus, humic acid can change the particle size distribution of the precipitated solids and larger particle formation is greatly inhibited by humic acid. This result indicates that existence of humic acid particles could diminish the performance of the flocculation/sedimentation process with higher effluent turbidity.

##**Previous Work**

In past semesters, the humic acid subteam experimented with humic acid dosages of 5 mg/L and 10 mg/L with various coagulant dosages. The team concluded that the optimal dosage for 5 mg/L of humic acid was between 1.6 mg/L and 1.8 mg/L of coagulant, while the 10 mg/L of humic acid was best treated by 1.3 mg/L. From these trials, the team concluded that as humic acid concentration increased coagulant dosage should decrease in order to maximize humic acid removal from the water; therefore, a negative linear relationship between the two variables. The Fall 2019 humic acid subteam began to test humic acid concentrations of 15 mg/L, 20 mg/L, and 25 mg/L; however, had not determined the optimal coagulant dosages for these concentrations. This team did conclude that above 2.1-2.3 mg/L of coagulant, the coagulant became less effective, and therefore, the effectiveness of coagulant levels out as it increases. This team and the Fall 2020 subteam began to confirm the linear results of the previous subteams; however, did not have time to draw conclusions.

##**Methods**

For experimental research so far, the flow rates for the water, coagulant and humic acid were determined for various concentrations of humic acid within the water. This task was accomplished using the Python code outlined in the Manual Section. From this code, a table was generated to for various coagulant dosages at three different concentrations of humic acid. ProCoDa was used to define set points on how long experiments should be run.



<img src="https://raw.githubusercontent.com/AguaClara/humic_acid/master/Fall%202018/Setup.jpg" height = 300 />

**Figure 1: Experimental Apparatus (Schematic Drawing)**

To standardize with setup of other particle-removal subteams, 1-inch clear PVC pipes were chosen and fabricated so that the experimental apparatus has a 50 cm recirculator and 35 cm tube settler. The floc wire is 40 cm and the bent angle of the tube settler is angled 60 degrees relative to the horizontal. The length of the tube settler was determined so that a capture velocity of  0.308 mm/s would be produced at the end of the reactor. The design is obtained from the High Rate Sedimentation subteam.

The HA flow and water flow are combined after leaving the pumps, and goes through the effluent turbidimeter to determine an initial turbidity. After leaving the turbidimeter, coagulant is added to the flow and enters the flocculator. Then the flow goes into the sedimentation tank where flocs are formed, and separated into two directions: the clean water goes through the top part of the sedimentation tank and pumped into the spectrophotometer, effluent turbidimeter and lastly exits the system through the wastewater pipe; the flocs are settled and directly leaves the sedimentation tank and into the wastewater flow.

##**Results and Analysis on Previous Work**
Through literature review, the team discovered that research done by a group of Cornell professors and graduate students discredited the negative linear relationship between humic acid concentration and coagulant dosage. (Du et. al.) describes the relationship as a positive linear relationship, in which coagulant dosage increases when humic acid presence in water is increased.


<img src= "https://lh3.googleusercontent.com/ambz5vswC4PsstALT9CXEqEpDVxyoWzUw-auVQ83mbX-La7uFr5SGkV8-Z03A9fsscCAxKt4gVGXSgUQOpaeZ2JMKmpGQTxxAE2IwKKgmrts10U77Iu_7uQCjYGwlVeBsxGkN49x" height = 300 />

**Figure 2:Effluent Turbidity as a Function of Time Fraction at 5 mg/L of Humic Acid**

<img src= "https://github.com/AguaClara/humic_acid/blob/master/Fall%202018/exp2.png?raw=true" height = 300 />

**Figure 3: Effluent Turbidity as a Function of Time Fraction at 10 mg/L of Humic Acid with Various Dosages of Coagulant**

In the above figures, the Fall 2018 subteam graphed the effluent turbidity vs. time for 5 mg/L and 10 mg/L of humic acid at various coagulant dosages. After reanalyzing the data, their conclusions about the optimal coagulant dosage decreasing with increased humic acid are supported by the figures; however, they are underresearched. The 10 mg/L humic acid removal trials only test 4 coagulant dosages below the optimal dosage for 5 mg/L of humic acid. Without data at higher coagulant dosages, the optimal coagulant dosage cannot be confirmed. In conclusion, the reanalysis of past data demonstrates that the determined linear relationship by past subteams does not have enough supporting experimental data to confirm that there is in fact a negative linear relationship especially when (Du et. al.) research states otherwise. Additionally, not enough trials at 15 mg/L. 20 mg/L and 25 mg/L of humic acid with varying coagulant dosages can be used to confirm or deny the linear relationship.

##**Coagulant Trials**


<img src="https://lh3.googleusercontent.com/sRoT5ER3FadmTNnOB6ItCAtdkGxC8TuObwJbVt43HSR1LIGS82clu5s60B787OYZcDhOYuslU5tmdp4-58TJEBgvpGh6WLB_qATnLBBVatVGqtJ6qmfn-LCQBXgt9Dp1WScGW0U0" height = 300 />

**Table 1: Concentrations of Humic Acid, Optimal Coagulant Dosage (Predicted From Past Experiments), and the Humic Acid, Coagulant and Water Flow Rates**


<img src="https://lh3.googleusercontent.com/qq4ACO8-qHY4bCVKki0rR80LxKqTcJ8Phrb90t4SgCB8zq9u7_e0TMv__W3XXoTg7pkClZs0iUvnAJVYQmfZr_wtTxoicUdVZ1LKS3qaT_q7gze9Bu8936gez8UlIx0ShW5Bxf07" height = 800 />
<img src="https://lh3.googleusercontent.com/xETWO7X2ib-u-o7D3f0iVXkVA_WdQZLxWnge0XaAQSA7AA9GL2uJoVTpeJEC77xfvjhIC7JE_vxwVAojF4xaIzJLeSCdoaL6RGSj3Ttg" height = 290, />


**Table 2: Varied Concentrations of Coagulant Dosage, for 15 mg/L, 20 mg/L and 25 mg/L of Humic Acid and the Respective Flow Waters in Rev/Min**

The team this semester has focused on lab procedure and experimental design to smooth the process of getting into the lab once it is available to the team. In constructing the experimental design, the subteam’s initial goal was to test varying coagulant dosages at 15 mg/L, 20 mg/L, and 25 mg/L of humic acid and continue the work of the Fall 2019 subteam. Using the provided python code, the team determined the required ProCoDa inputs for the humic acid, coagulant, and water pumps, in order to test 15 coagulant dosages for the 3 humic acid concentrations. The team expects that the optimal coagulant dosage for each humic acid concentration will be displayed by the graph that minimizes absorbance after reaching a steady-state flow. Additionally, the subteam expects that the data will disprove the relationship found by past subteams between humic acid concentration and coagulant dosage. The optimal coagulant dosage should linearly increase with increasing humic acid concentration.

The subteam also identified the expected optimal coagulant dosages for each humic acid concentration based on the negative linear relationship that past subteams identified. For 15 mg/L this value was 1.0 mg/L of coagulant, for 20 mg/L the value was 0.7 mg/L of coagulant and for 25 mg/L, this value was expected to be 0.4 mg/L of coagulant. Based on these values, the team concluded that 0.4 mg/L of coagulant seems like a small dosage to treat such a high concentration of humic acid; therefore, the subteam predicts further experimentation will show that this dosage is in fact too low and that the relationship is incorrect.

The subteam also investigated the ProCoDa Method and set points written by past semester's teams. Without the physical pumps and experimental setup, the team optimized the requirements for each set point so that it would theoretically run smoothly in lab; however, there were requirements such as com port 1 that were selected for certain set points that made the data not match. The subteam would hope to investigate this discrepancy and determined whether this requirement is necessary for the pump set points once the team gets into lab.

## **Current Work**
When setting up the apparatus, the Fall 2021 subteam had issues with connectivity and leaking of the tubing. Components such as tubing and connectors were switched out to fix the leaking of the setup. After the apparatus was constructed, the team had issues with the hardware of the computer, software with ProCoDa, and connectivity with the setup.

The hardware issue was resolved by upgrading the RAM of the PC, adding a wifi router, and updating Windows of the computer. By reffering to the ProCoDa manual, the team was also able to fix the interconnection issue between the apparatus and ProCoDa by determining the correct COM port and resetting all the pump IDs. The team then created a new ProCoDa file with new setpoints to run experiments. At first, the pumps did not run, but changing the order of the setpoints fixed this issue. It was found that the setpoints required, such as COM port, pump ID/address, and flow rate, for setting the "control" setpoints ("coagulant control" for instance) need to be in the exact order as described by ProCoDa. In addition, after successfully connecting the apparatus to ProCoDa, the solution was not leaving the influent turbidimeter when test trials were run. This was resolved by connecting the turbidimeter to the COM port after noticing the disconnection. Currently, the team is working on expediting the process with our set up since it takes hours for experiments to run from start to finish.

## **Future Work**
This semester, the major goals for this team are to validate a postive relationship betweeen humic acid concentration and coagulant dosage and to define a steady state at which the data can be collected and to determine the optimal coagulant concentration for water samples with varying humic acid concentrations. Another goal for this semester is to design an automated ProCoDa code that would allow experiments to run for longer periods of time without having to be physically present to start and stop the reaction.

## **Conclusion**

The goal for future semesters is to fully implement the aforementioned future work and experimental procedure. The group will assess the previously established linear association from the last Humic Acid Removal subteam whilst having in mind that it is likely that a strong negative association is incorrect. Additionally, the team will also implement our plan to re-run previous experiments with more varying concentrations of coagulant and humic acid in order to better understand the coagulant:humic acid ratio. Lastly, the team concludes that the implementation of a ProCoDa code that allows to control the experimental setup from a distance would be most beneficial, as it would allow to perform a larger amount of experiments in a reduced window of time.

##**Manual**

Before running trials, ensure that the humic acid Experiemental SetUp is complete with the following items:

1. 4 pumps (coagulant, HA, effluent water, influent water)
2. Sedimentation Tank
3. 2 Turbidimeters
4. Spectrophotometer
5. Micro-tubing & 1/4" tubing
6. 1” Clear PVC for recirculator/ tube settler
7. 60-degree bent tubing for tube settler
8. HA Stock Solution
9. Coagulant Stock Solution
10. Kaolin Clay

After acquiring each of these items, use the code below to determine the flow rates for the desired humic acid concentration and coagulant dosage.

Afterwards, use the below procedure to execute the trials.

###**Procedure**

To run the experiment we:

1. Clean the flocculator tube and the effluent turbidimeter and spectrophotometer by flushing it with a steady stream of water
2. Drain the recirculation unit
3. Decide a coagulant and humic acid concentration to test
4. Input the value into the python code, which outputs the necessary pump speed (Using the below code for this step)
5. Enter the humic acid concentration for the experiment into python code, which outputs the necessary humic acid pump speed
6. Fill both humic acid and coagulant stock buckets with at least 3-4 litres
7. Turn on the the water pump, the coagulant pump and the humic acid pump
8. The coagulant and humic acid pump speed is controlled by ProCoDa. The water pump is generally manually set to run at 50 RPM or the value calculated in the previous code. However, the value for the water pump RPM should always be less than 50.

###**ProCoDa Method**
The following ProCoDa method can be used to control the pumps, turbidimeters, and spectrometer in the experimental set up. The set points shown in Table 3 describe the ProCoDa method.

* Now you can configure a Golander pump using the Rule Editor. The external code for Golander pumps requires 4 inputs: pump address, on state, pump (ml/rev), and flow (mL/s).

<img src="https://github.com/AguaClara/humic_acid/blob/master/Set%20Points.JPG?raw=true" />

**Table 3: Value/ Unit and Purpose of each set point used in the ProCoDa Method**

##**Python Code**
"""

!pip install aguaclara
import aguaclara as ac
from aguaclara.core.units import u
import matplotlib.pyplot as plt
import numpy as np


# Recirculator:
# velocity = 1 mm/s
# total flow rate = velocity * cross sectional area
r = 12.7 * u.mm
vt = 1 * u.mm / u.s
a = np.pi*(r**2)
qt = vt * a

# Humic acid:
# stock flow rate HA = total flow rate HA * desired concentration HA / stock concentration HA
cHAs = 0.25 * u.g / u.L
cHAd = 0.015 * u.g / u.L
qHAs = qt * cHAd / cHAs

# Coagulant:
# stock flow rate coag = total flow rate coag * desired concentration coag / stock concentration coag
cCGs = 0.5 * u.g / u.L
cCGd = 0.0004 * u.g / u.L
qCGs = qt * cCGd / cCGs

# Water:
# total flow rate = stock flow rate HA + stock flow rate Coag + water flow rate
qW = qt - qCGs - qHAs

vHA = ac.vol_per_rev_3_stop('yellow-blue')
sHA = qHAs.to(u.ml/u.s) / vHA

vCG = ac.vol_per_rev_3_stop('yellow-blue')
sCG = qCGs.to(u.ml/u.s) / vHA

vW = ac.vol_per_rev_LS(17)
sW = qW.to(u.ml/u.s) / vW

print("  ")
print("Humic acid: " + str(sHA.to(u.rpm)))
print("Coagulant: " + str(sCG.to(u.rpm)))
print("Water: " + str(sW.to(u.rpm)))

"""##**Variables**
The variables defined in the code above have the following meanings:

$ vt $: upflow velocity in the recirculator

$ r $: radius of the recirculator tube

$ a $: cross sectional area of the recirculator tube

$ qt $: flow rate through the recirculator

$ cHAs $: stock humic acid concentration (into humic acid pump)

$ cHAd $: desired humic acid concentration in the recirculator

$ qHAs $: stock humic acid flow rate (through humic acid pump)

$ cCGs $: stock coagulant concentration (into coagulant pump)

$ cCGd $: desired coagulant concentration in the recirculator

$ qCGs $: stock coagulant flow rate (through coagulant pump)

$ qW $: flow rate of water in the recirculator

$ vHA $: volume per revolution of the humic acid pump (dependent on pump tubing)

$ sHA $: revolution per second (pump speed) of the humic acid pump

$ vCG $: volume per revolution of the coagulant pump (dependent on pump tubing)

$ sCG $: revolution per second (pump speed) of the coagulant pump

$ vW $: volume per revolution of the water pump (dependent on pump tubing)

$ sW $: revolution per second (pump speed) of the water pump

## Bibliography
Logan, B. E., Hermanowicz, S. W., & Parker,A. S. (1987). A Fundamental Model for Trickling Filter Process Design. Journal (Water Pollution Control Federation), 59(12), 1029–1042.

Du, Y., Pennock, W. H., Weber-Shirk, M. L., & Lion, L. W. (2019). Observations and a Geometric Explanation of Effects of Humic Acid on Flocculation. Environmental Engineering Science, 36(5), 614–622. https://doi.org/10.1089/ees.2018.0405

Matilaninen, A, Vepsalainen, M & Sillanpaa, M. (2010). Natural Organic Matter Removal by Coagulation during Drinking Water Treatment. Adv Colloid Interface Sci.

Soh, YC, Roddick, F & Van Leeuwen, J. (2008). The Impact of Alum Coagulation on the Character, Biodegradability and Disinfection By-product Formation Potential of Reservoir Natural Organic Matter (NOM) Fractions. Water Sci Technol. 58(6), 1173-9.

Kopfler, F., H. Ringhand, W. Coleman, AND J. Meier. REACTIONS OF CHLORINE IN DRINKING WATER, WITH HUMIC ACIDS AND 'IN VIVO'. U.S. Environmental Protection Agency, Washington, D.C., EPA/600/D-84/196 (NTIS PB85160737).

Zhang, Panyue, et al. (2008). Coagulation Characteristics of Polyaluminum Chlorides PAC-Al30 on Humic Acid Removal from Water. Journal (Separation and Purification Technology), 63(3), 642-646.

Thomas Bradford, Bridget Childs, Matt Lee, and Carolyn Wang. Spring 2020 Humic Acid Removal Subteam Report
https://docs.google.com/document/d/1-J-1yz4XMk7PfWRVjXXm-48p_qRwkSfPGgqAyD6LdlA/edit?usp=sharing
"""