setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DeepaRichardson/Data/Entries to Criterion/Reversal/WTmale/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
WTmale <- dataset
write.csv(WTmale, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DeepaRichardson/Spreadsheets/WTmaleRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DeepaRichardson/Data/Entries to Criterion/Reversal/WTfemale/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
WTfemale <- dataset
write.csv(WTfemale, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DeepaRichardson/Spreadsheets/WTfemaleRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DeepaRichardson/Data/Entries to Criterion/Reversal/SOD1KOmale/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
SOD1KOmale <- dataset
write.csv(SOD1KOmale, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DeepaRichardson/Spreadsheets/SOD1KOmaleRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DeepaRichardson/Data/Entries to Criterion/Reversal/SOD1KOfemale/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
SOD1KOfemale <- dataset
write.csv(SOD1KOfemale, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DeepaRichardson/Spreadsheets/SOD1KOfemaleRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Consolidated/Data/Entries to Criterion/Reversal/old/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
old <- dataset
write.csv(old, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Consolidated/Spreadsheets/oldRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Reversal/MCTRL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MCTRL <- dataset
write.csv(MCTRL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MCTRLRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Reversal/MAL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MAL <- dataset
write.csv(MAL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MALRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Reversal/MDR/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MDR <- dataset
write.csv(MDR, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MDRRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Reversal/FCTRL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FCTRL <- dataset
write.csv(FCTRL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FCTRLRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Reversal/FAL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FAL <- dataset
write.csv(FAL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FALRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Reversal/FDR/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FDR <- dataset
write.csv(FDR, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FDRRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/MCTRL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MCTRL <- dataset
write.csv(MCTRL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MCTRLIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/MAL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MAL <- dataset
write.csv(MAL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MALIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/MDR/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MDR <- dataset
write.csv(MDR, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MDRIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/FCTRL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FCTRL <- dataset
write.csv(FCTRL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FCTRLIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/FAL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FAL <- dataset
write.csv(FAL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FALIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/FDR/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FDR <- dataset
write.csv(FDR, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FDRIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Sonntag/Data/Entries to Criterion/Initial Discrimination/young/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
young <- dataset
write.csv(young, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Sonntag/Spreadsheets/youngIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Sonntag/Data/Entries to Criterion/Initial Discrimination/middle/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
middle <- dataset
write.csv(middle, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Sonntag/Spreadsheets/middleIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Sonntag/Data/Entries to Criterion/Initial Discrimination/old/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
old <- dataset
write.csv(old, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Sonntag/Spreadsheets/oldIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/YNGSCRAM/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
YNGSCRAM <- dataset
write.csv(YNGSCRAM, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/YNGSCRAMRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/YNGAB/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
YNGAB <- dataset
write.csv(YNGAB, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/YNGABRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/OLDSCRAM/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
OLDSCRAM <- dataset
write.csv(OLDSCRAM, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/OLDSCRAMRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/OLDAB/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
OLDAB <- dataset
write.csv(OLDAB, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/OLDABRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/YNGSALSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
YNGSALSet03 <- dataset
write.csv(YNGSALSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/YNGSALSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/YNGABSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
YNGABSet03 <- dataset
write.csv(YNGABSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/YNGABSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/OLDSALSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
OLDSALSet03 <- dataset
write.csv(OLDSALSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/OLDSALSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/OLDSCRAMSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
OLDSCRAMSet03 <- dataset
write.csv(OLDSCRAMSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/OLDSCRAMSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/OLDABSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
OLDABSet03 <- dataset
write.csv(OLDABSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/OLDABSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Drevet/Data/Entries to Criterion/Reversal/WTCONTROL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
WTCONTROL <- dataset
write.csv(WTCONTROL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Drevet/Spreadsheets/WTCONTROLRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Drevet/Data/Entries to Criterion/Reversal/WTINFECTED/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
WTINFECTED <- dataset
write.csv(WTINFECTED, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Drevet/Spreadsheets/WTINFECTEDRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Drevet/Data/Entries to Criterion/Reversal/MIRCONTROL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MIRCONTROL <- dataset
write.csv(MIRCONTROL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Drevet/Spreadsheets/MIRCONTROLRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Drevet/Data/Entries to Criterion/Reversal/MIRINFECTED/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MIRINFECTED <- dataset
write.csv(MIRINFECTED, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Drevet/Spreadsheets/MIRINFECTEDRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/YNGSALSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
YNGSALSet03 <- dataset
write.csv(YNGSALSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/YNGSALSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/YNGABSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
YNGABSet03 <- dataset
write.csv(YNGABSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/YNGABSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/OLDSALSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
OLDSALSet03 <- dataset
write.csv(OLDSALSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/OLDSALSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/OLDSCRAMSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
OLDSCRAMSet03 <- dataset
write.csv(OLDSCRAMSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/OLDSCRAMSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Data/Entries to Criterion/Reversal/OLDABSet03/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
OLDABSet03 <- dataset
write.csv(OLDABSet03, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Yeganeh/Spreadsheets/OLDABSet03RevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DrevetsYabluchanskiy/Data/Entries to Criterion/Reversal/youngcontrolN/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
youngcontrolN <- dataset
write.csv(youngcontrolN, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DrevetsYabluchanskiy/Spreadsheets/youngcontrolNRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DrevetsYabluchanskiy/Data/Entries to Criterion/Reversal/younginfectedNlow/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
younginfectedNlow <- dataset
write.csv(younginfectedNlow, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/DrevetsYabluchanskiy/Spreadsheets/younginfectedNlowRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/MCTRL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MCTRL <- dataset
write.csv(MCTRL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MCTRLIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/MAL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MAL <- dataset
write.csv(MAL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MALIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/MDR/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MDR <- dataset
write.csv(MDR, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MDRIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/FCTRL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FCTRL <- dataset
write.csv(FCTRL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FCTRLIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/FAL/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FAL <- dataset
write.csv(FAL, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FALIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/FDR/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FDR <- dataset
write.csv(FDR, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FDRIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/MDRst/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MDRst <- dataset
write.csv(MDRst, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MDRstIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Initial Discrimination/FDRst/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FDRst <- dataset
write.csv(FDRst, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FDRstIDETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Reversal/MDRst/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
MDRst <- dataset
write.csv(MDRst, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/MDRstRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Data/Entries to Criterion/Reversal/FDRst/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
FDRst <- dataset
write.csv(FDRst, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Richardson/Spreadsheets/FDRstRevETCresults.csv")
rm(list = ls())

setwd("G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Resilience2020/Data/Entries to Criterion/Reversal/yngcontrolmale/")
file_list <- list.files()
for (i in file_list){
  # if the merged dataset does exist, append to it
  if (exists("dataset")){
    temp_dataset1 <- read.csv(i)
    dataset <- rbind(dataset, temp_dataset1)
    rm(temp_dataset1)
  }
  # if the merged dataset doesn't exist, create it
  if (!exists("dataset")){
    dataset <- read.csv(i)
  }
}
rm(i)
rm(file_list)
yngcontrolmale <- dataset
write.csv(yngcontrolmale, file="G:/Behavioral Data/Sonntag Lab Dropbox/Phenotyper/Investigators/Resilience2020/Spreadsheets/yngcontrolmaleRevETCresults.csv")
rm(list = ls())

