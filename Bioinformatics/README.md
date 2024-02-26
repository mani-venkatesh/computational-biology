### **Breast Cancer Drug Discovery Project using ChEMBL Databse**

*This project was inspired by the YouTube channel of [dataprofessor](https://www.youtube.com/dataprofessor)*

Breast cancer is a heterogeneous and often aggressive malignancy that originates in the breast tissue. It is characterized by the uncontrolled growth of abnormal cells in the breast, which can invade surrounding tissues and potentially spread to other parts of the body. In computational drug discovery for breast cancer, particular attention is given to targeting the Epidermal Growth Factor Receptor (EGFR) protein family. This family plays a crucial role in regulating cell proliferation, survival, and differentiation, and aberrant activation of EGFR signaling is frequently implicated in breast cancer progression, making it a promising target for the development of novel therapeutic interventions. *For the purposes of this project, only EGFR-targetting compounds with an IC50 < 100 nM were considered as active compounds.*

[ChEMBL Database](https://www.ebi.ac.uk/chembl/g/) is a large set of bioactivity data of different tested compounds on pathophysiological targets , compiled from scientific research papers. 

**Install ChEMBL webresource client library: $ pip install chembl_webresource_client [Github](https://github.com/chembl/chembl_webresource_client) [NIH](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489243/)** 

This library enables users with HTTPS protocol and caches results in local file systems for fast retrieval - based on Django QuerySet.

### Running Instructions
1. Prepare environment with packages from requirements.txt file
2. Run all cells in EGFR_data_collection.ipynb
3. Run all cells in EGFR_data_analysis.ipynb