
import os
import socket

config = dict()

config['template'] = 'run_job.sh'

# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======
if (socket.gethostname() == 'Lucys-MacBook-Pro-3.local') or (socket.gethostname() == 'vertex.kiewit.dartmouth.edu') or (socket.gethostname() == 'vertex.local'):
    config['datadir'] = '/Users/lucyowen/Desktop/supereeg_env/full_mats/results/'
    config['workingdir'] = '/Users/lucyowen/Desktop/supereeg_env/ave_mats/'
    config['startdir'] = '/Users/lucyowen/Desktop/supereeg_env/'  # directory to start the job in
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job_local.sh')
else:
    config['datadir'] = '/idata/cdl/lowen/full_mats/results/'
    config['workingdir'] = '/idata/cdl/lowen/ave_mats'
    config['startdir'] = '/idata/cdl/lowen'
    config['template'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'run_job.sh')

# job creation options
config['scriptdir'] = os.path.join(config['workingdir'], 'scripts')
config['lockdir'] = os.path.join(config['workingdir'], 'locks')
config['resultsdir'] = os.path.join(config['workingdir'], 'results')
config['pyFRlocsdir'] = os.path.join(config['startdir'], 'pyFR_locs/results')

# runtime options
config['jobname'] = "ave_mats"  # default job name
config['q'] = "default"  # options: default, testing, largeq
config['nnodes'] = 4  # how many nodes to use for this one job
config['ppn'] = 4  # how many processors to use for this one job (assume 4GB of RAM per processor)
config['walltime'] = '10:00:00'  # maximum runtime, in h:MM:SS
#config['startdir'] = '/ihome/lowen/repos/supereeg/examples'  # directory to start the job in
config['cmd_wrapper'] = "python"  # replace with actual command wrapper (e.g. matlab, python, etc.)
config['modules'] = "(\"python/2.7.11\")"  # separate each module with a space and enclose in (escaped) double quotes
# ====== MODIFY ONLY THE CODE BETWEEN THESE LINES ======