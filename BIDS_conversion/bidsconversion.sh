
######################################################################################################################################
"""
# @Author: Nichollette Acosta
# @Title: Bids Converter
# @Description:  This will shell into our singularity image and run the heudiconv converter
#                on our data
"""
######################################################################################################################################

# RUN SINGULARITY --
# Right now I have a singularity shell ..... look into making a run file for This

singularity shell -B /projects/niblab/test:/test heudiconv.simg



cd /lab_data/SugarMama
files=(SM*)
cd ../../
num=0
for f in ${files[@]};do
num=$(($num+1))
value=$(printf "%02d" $num)
export value
heudiconv -b -d /lab_data/SugarMama2/{subject}/raw/{subject}/*/*.dcm -s $f -f /test/heuristic_converter00.py -c dcm2niix -b  -o /test/output/SugarMama2/sub-${value}
echo $value
done
