# IC HW5

- [IC HW5](#ic-hw5)
  - [Problem 1](#problem-1)
    - [Original Setup](#original-setup)
      - [Model](#model)
      - [Hyperparameter](#hyperparameter)
      - [Accuracy Train History](#accuracy-train-history)
      - [Loss Train History](#loss-train-history)
      - [Test Accuracy](#test-accuracy)
      - [Confusion Matrix](#confusion-matrix)
    - [Modified Setup](#modified-setup)
      - [Model](#model-1)
      - [Hyperparameter](#hyperparameter-1)
      - [Accuracy Train History](#accuracy-train-history-1)
      - [Loss Train History](#loss-train-history-1)
      - [Test Accuracy](#test-accuracy-1)
      - [Confusion Matrix](#confusion-matrix-1)
  - [Problem 2](#problem-2)
    - [Original Setup](#original-setup-1)
      - [Model](#model-2)
      - [Hyperparameter](#hyperparameter-2)
      - [Accuracy Train History](#accuracy-train-history-2)
      - [Loss Train History](#loss-train-history-2)
      - [Test Accuracy](#test-accuracy-2)
      - [Confusion Matrix](#confusion-matrix-2)
    - [Modified Setup](#modified-setup-1)
      - [Model](#model-3)
      - [Hyperparameter](#hyperparameter-3)
      - [Accuracy Train History](#accuracy-train-history-3)
      - [Loss Train History](#loss-train-history-3)
      - [Test Accuracy](#test-accuracy-3)
      - [Confusion Matrix](#confusion-matrix-3)


## Problem 1

### Original Setup

#### Model

![](Figures/P1_Original_Setup_Model.png)

#### Hyperparameter

| **Item** | **Value** |
|-----------|----------|
| **Optimize**   | Adam    |
| **validation_split** | 0.2    |
| **epochs**   | 20    |
| **batch_size**   | 300    |


#### Accuracy Train History

![](Figures/P1_Original_Setup_ACC_TrainHistory.jpg)

#### Loss Train History

![](Figures/P1_Original_Setup_LOSS_TrainHistory.jpg)

#### Test Accuracy
0.9919999837875366

#### Confusion Matrix

|label|0|1|2|3|4|5|6|7|8|9|
|---|---|---|---|---|---|---|---|---|---|---|
|0|975|0|1|0|0|1|1|1|1|0|
|1|0|1129|0|2|0|0|0|3|1|0|
|2|0|0|1025|0|0|0|0|6|1|0|
|3|0|0|1|1006|0|1|0|0|2|0|
|4|0|0|0|0|980|0|1|0|0|1|
|5|2|0|0|8|0|880|1|0|0|1|
|6|3|2|1|0|2|2|945|0|3|0|
|7|0|1|1|1|0|0|0|1023|1|1|
|8|3|0|2|0|0|0|0|0|968|1|
|9|0|1|1|1|10|4|0|3|2|987|


### Modified Setup

- Replacing all "relu" activation with "elu" could increase accuracy to 0.9933.
- Adding another hiden layer with 64 unit doesn't seems to help.
- Reducing dropout rate also has no positive effect.

#### Model

![](Figures/P1_Mod_Model.png)

#### Hyperparameter

| **Item** | **Value** |
|-----------|----------|
| **Optimize**   | Adam    |
| **validation_split** | 0.2    |
| **epochs**   | 20    |
| **batch_size**   | 300    |

#### Accuracy Train History

![](Figures/P1_Mod_Accu.png)

#### Loss Train History

![](Figures/P1_Mod_loss.png)

#### Test Accuracy

0.9933000206947327

#### Confusion Matrix




## Problem 2

### Original Setup

#### Model

![](Figures/P2_Original_Setup_Model.png)

#### Hyperparameter

| **Item** | **Value** |
|-----------|----------|
| **Optimize**   | Adam    |
| **validation_split** | 0.2    |
| **epochs**   | 10    |
| **batch_size**   | 128    |


#### Accuracy Train History

![](Figures/P2_Original_Setup_ACC_TrainHistory.jpg)

#### Loss Train History

![](Figures/P2_Original_Setup_LOSS_TrainHistory.jpg)


#### Test Accuracy
0.7432000041007996

#### Confusion Matrix

|label|0|1|2|3|4|5|6|7|8|9|
|---|---|---|---|---|---|---|---|---|---|---|
|0|749|14|54|14|10|9|13|8|91|38|
|1|11|848|13|6|4|5|10|2|32|69|
|2|57|3|701|37|86|33|49|16|10|8|
|3|18|9|102|523|81|160|54|20|22|11|
|4|16|3|89|54|742|18|33|32|12|1|
|5|12|1|79|165|65|609|24|36|8|1|
|6|2|4|59|46|36|20|823|1|8|1|
|7|15|3|51|27|70|46|9|766|5|8|
|8|38|17|25|6|10|9|5|1|872|17|
|9|21|71|15|13|6|13|9|13|40|799|



### Modified Setup


#### Model

![](Figures/P2_Modified_Setup_Model.png)


#### Hyperparameter

| **Item** | **Value** |
|-----------|----------|
| **Optimize**   | Adam    |
| **validation_split** | 0.2    |
| **epochs**   | 100    |
| **batch_size**   | 128    |

#### Accuracy Train History

![](Figures/P2_Modified_Setup_ACC_TrainHistory.jpg)

#### Loss Train History

![](Figures/P2_Modified_Setup_LOSS_TrainHistory.jpg)

#### Test Accuracy

0.8543000221252441

#### Confusion Matrix

|label|0|1|2|3|4|5|6|7|8|9|
|---|---|---|---|---|---|---|---|---|---|---|
|0|870|25|7|10|6|0|4|8|17|53|
|1|2|944|0|1|0|0|0|0|1|52|
|2|56|9|750|35|39|13|54|19|3|22|
|3|7|10|23|747|25|53|54|22|11|48|
|4|7|2|29|16|842|8|40|44|2|10|
|5|7|6|15|115|18|734|43|25|5|32|
|6|4|6|7|9|8|1|945|3|3|14|
|7|9|7|7|12|14|15|8|896|2|30|
|8|49|41|4|1|1|0|4|0|865|35|
|9|5|39|0|0|1|1|1|1|2|950|