#

# Get required input from command line
while getopts "u:p:s:i:o:d:h:" opt; do
  case $opt in
    u) username="$OPTARG";;
    p) password="$OPTARG";;
    s) subject_name="$OPTARG";;
    i) input_dir="$OPTARG";;
    o) output_dir="$OPTARG";;
    d) dicom_dir="$OPTARG";;
    h) hpc_address="$OPTARG";;
  esac
done


# log on to the HPC Cluster
# will need an HPC address and a password from the username
ssh -XY $hpc_address
sshpass -p $password



# pull container from singularity hub

# run singularity container
singularity shell -B $input_dir:/test -B output_dir heudiconv.simg

# change to the data directory
cd /test
# grab folder names to iterate over
files=(*)

# assign counter for filename purposes
# --possible customization in the future
num=0

# iterate over folders and convert dicoms to bids
for f in ${files[@]};do
num=$(($num+1))
value=$(printf "%02d" $num)
export value
heudiconv -b -d /lab_data/SugarMama2/{subject}/raw/{subject}/*/*.dcm -s $f -f /test/heuristic_converter00.py -c dcm2niix -b  -o /test/output/SugarMama2/sub-${value}
echo $value
done
