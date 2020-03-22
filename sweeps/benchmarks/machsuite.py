# MachSuite benchmark definitions.

from datatypes import *
from params import *

aes_aes = Benchmark("aes_aes", "aes/aes")
aes_aes.set_kernels(["aes256_encrypt_ecb"])
aes_aes.set_main_id(0x00000010)
aes_aes.add_array("ctx", 96, 1)
aes_aes.add_array("k", 32, 1)
aes_aes.add_array("buf", 16, 1)
aes_aes.add_array("rcon", 1, 1)
aes_aes.add_array("sbox", 256, 1)
aes_aes.add_loop("aes_addRoundKey_cpy", "cpkey")
aes_aes.add_loop("aes_subBytes", "sub")
aes_aes.add_loop("aes_addRoundKey", "addkey")
aes_aes.add_loop("aes_expandEncKey", "exp1")
aes_aes.add_loop("aes_expandEncKey", "exp2")
aes_aes.add_loop("aes_mixColumns", "mix")
aes_aes.add_loop("aes256_encrypt_ecb", "ecb1")
aes_aes.add_loop("aes256_encrypt_ecb", "ecb2")
aes_aes.add_loop("aes256_encrypt_ecb", "ecb3")
aes_aes.add_required_files(["input.data", "check.data"])
aes_aes.set_exec_cmd("aes_aes-gem5-accel")

bfs_bulk = Benchmark("bfs_bulk", "bfs/bulk")
bfs_bulk.set_kernels(["bfs"])
bfs_bulk.set_main_id(0x00000030)
bfs_bulk.add_array("nodes", 512, 8)
bfs_bulk.add_array("edges", 4096, 8)
bfs_bulk.add_array("level", 256, 1)
bfs_bulk.add_array("level_counts", 10, 8)
bfs_bulk.add_loop("bfs", "loop_horizons")
bfs_bulk.add_loop("bfs", "loop_nodes")
bfs_bulk.add_loop("bfs", "loop_neighbors")
bfs_bulk.add_required_files(["input.data", "check.data"])
bfs_bulk.set_exec_cmd("bfs_bulk-gem5-accel")

bfs_queue = Benchmark("bfs_queue", "bfs/queue")
bfs_queue.set_kernels(["bfs"])
bfs_queue.set_main_id(0x00000040)
bfs_queue.add_array("queue", 256, 8)
bfs_queue.add_array("nodes", 512, 8)
bfs_queue.add_array("edges", 4096, 8)
bfs_queue.add_array("level", 256, 1)
bfs_queue.add_array("level_counts", 10, 8)
bfs_queue.add_loop("bfs", "loop_queue")
bfs_queue.add_loop("bfs", "loop_neighbors")
bfs_queue.add_required_files(["input.data", "check.data"])
bfs_queue.set_exec_cmd("bfs_queue-gem5-accel")

fft_strided = Benchmark("fft_strided", "fft/strided")
fft_strided.set_kernels(["fft"])
fft_strided.set_main_id(0x00000050)
fft_strided.add_array("real", 1024, 8)
fft_strided.add_array("img", 1024, 8)
fft_strided.add_array("real_twid", 1024, 8)
fft_strided.add_array("img_twid", 1024, 8)
fft_strided.add_loop("fft", "outer")
fft_strided.add_loop("fft", "inner")
fft_strided.add_required_files(["input.data", "check.data"])
fft_strided.set_exec_cmd("fft_strided-gem5-accel")

fft_transpose = Benchmark("fft_transpose", "fft/transpose")
fft_transpose.set_kernels(["fft1D_512"])
fft_transpose.set_main_id(0x00000060)
fft_transpose.add_function_array("twiddles8", "reversed8", 8, 4)
fft_transpose.add_array("DATA_x", 512, 8)
fft_transpose.add_array("DATA_y", 512, 8)
fft_transpose.add_array("data_x", 8, 8)
fft_transpose.add_array("data_y", 8, 8)
fft_transpose.add_array("smem", 576, 8)
fft_transpose.add_array("work_x", 512, 8)
fft_transpose.add_array("work_y", 512, 8)
fft_transpose.add_loop("fft1D_512", "loop1")
fft_transpose.add_loop("fft1D_512", "loop2")
fft_transpose.add_loop("fft1D_512", "loop3")
fft_transpose.add_loop("fft1D_512", "loop4")
fft_transpose.add_loop("fft1D_512", "loop5")
fft_transpose.add_loop("fft1D_512", "loop6")
fft_transpose.add_loop("fft1D_512", "loop7")
fft_transpose.add_loop("fft1D_512", "loop8")
fft_transpose.add_loop("fft1D_512", "loop9")
fft_transpose.add_loop("fft1D_512", "loop10")
fft_transpose.add_loop("fft1D_512", "loop11")
fft_transpose.add_loop("fft1D_512", "twiddles")
fft_transpose.add_required_files(["input.data", "check.data"])
fft_transpose.set_exec_cmd("fft_transpose-gem5-accel")

gemm_blocked = Benchmark("gemm_blocked", "gemm/blocked")
gemm_blocked.set_kernels(["bbgemm"])
gemm_blocked.set_main_id(0x00000070)
gemm_blocked.add_array("m1", 4096, 4)
gemm_blocked.add_array("m2", 4096, 4)
gemm_blocked.add_array("prod", 4096, 4)
gemm_blocked.add_loop("bbgemm", "loopjj")
gemm_blocked.add_loop("bbgemm", "loopkk")
gemm_blocked.add_loop("bbgemm", "loopi")
gemm_blocked.add_loop("bbgemm", "loopk")
gemm_blocked.add_loop("bbgemm", "loopj")
gemm_blocked.add_required_files(["input.data", "check.data"])
gemm_blocked.set_exec_cmd("gemm_blocked-gem5-accel")

gemm_ncubed = Benchmark("gemm_ncubed", "gemm/ncubed")
gemm_ncubed.set_kernels(["gemm"])
gemm_ncubed.set_main_id(0x00000080)
gemm_ncubed.add_array("m1", 4096, 4)
gemm_ncubed.add_array("m2", 4096, 4)
gemm_ncubed.add_array("prod", 4096, 4)
gemm_ncubed.add_loop("gemm", "outer")
gemm_ncubed.add_loop("gemm", "middle")
gemm_ncubed.add_loop("gemm", "inner")
gemm_ncubed.add_required_files(["input.data", "check.data"])
gemm_ncubed.set_exec_cmd("gemm_ncubed-gem5-accel")

kmp_kmp = Benchmark("kmp_kmp", "kmp/kmp")
kmp_kmp.set_kernels(["kmp"])
kmp_kmp.set_main_id(0x00000090)
kmp_kmp.add_array("pattern", 4, 1)
kmp_kmp.add_array("input", 32411, 1)
kmp_kmp.add_array("kmpNext", 4, 4)
kmp_kmp.add_array("n_matches", 1, 4)
kmp_kmp.add_loop("CPF", "c1")
kmp_kmp.add_loop("CPF", "c2")
kmp_kmp.add_loop("kmp", "k1")
kmp_kmp.add_loop("kmp", "k2")
kmp_kmp.add_required_files(["input.data", "check.data"])
kmp_kmp.set_exec_cmd("kmp_kmp-gem5-accel")

md_grid = Benchmark("md_grid", "md/grid")
md_grid.set_kernels(["md"])
md_grid.set_main_id(0x000000A0)
md_grid.add_array("n_points", 64, 4)
md_grid.add_array("force", 1920, 8)
md_grid.add_array("position", 1920, 8)
md_grid.add_loop("md", "loop_grid0_x")
md_grid.add_loop("md", "loop_grid0_y")
md_grid.add_loop("md", "loop_grid0_z")
md_grid.add_loop("md", "loop_grid1_x")
md_grid.add_loop("md", "loop_grid1_y")
md_grid.add_loop("md", "loop_grid1_z")
md_grid.add_loop("md", "loop_p")
md_grid.add_loop("md", "loop_q")
md_grid.add_required_files(["input.data", "check.data"])
md_grid.set_exec_cmd("md_grid-gem5-accel")

md_knn = Benchmark("md_knn", "md/knn")
md_knn.set_kernels(["md_kernel"])
md_knn.set_main_id(0x000000B0)
md_knn.add_array("force_x", 256, 8)
md_knn.add_array("force_y", 256, 8)
md_knn.add_array("force_z", 256, 8)
md_knn.add_array("position_x", 256, 8)
md_knn.add_array("position_y", 256, 8)
md_knn.add_array("position_z", 256, 8)
md_knn.add_array("NL", 4096, 8)
md_knn.add_loop("md_kernel", "loop_i")
md_knn.add_loop("md_kernel", "loop_j")
md_knn.add_required_files(["input.data", "check.data"])
md_knn.set_exec_cmd("md_knn-gem5-accel")

nw_nw = Benchmark("nw_nw", "nw/nw")
nw_nw.set_kernels(["needwun"])
nw_nw.set_main_id(0x000000C0)
nw_nw.add_array("SEQA", 128, 1)
nw_nw.add_array("SEQB", 128, 1)
nw_nw.add_array("alignedA", 256, 1)
nw_nw.add_array("alignedB", 256, 1)
nw_nw.add_array("M", 16641, 4)
nw_nw.add_array("ptr", 16641, 1)
nw_nw.add_loop("needwun", "init_row")
nw_nw.add_loop("needwun", "init_col")
nw_nw.add_loop("needwun", "fill_out")
nw_nw.add_loop("needwun", "fill_in")
nw_nw.add_loop("needwun", "trace")
nw_nw.add_loop("needwun", "pad_a")
nw_nw.add_loop("needwun", "pad_b")
nw_nw.add_required_files(["input.data", "check.data"])
nw_nw.set_exec_cmd("nw_nw-gem5-accel")

sort_merge = Benchmark("sort_merge", "sort/merge")
sort_merge.set_kernels(["mergesort"])
sort_merge.set_main_id(0x000000D0)
sort_merge.add_array("temp", 4096, 4)
sort_merge.add_array("a", 4096, 4)
sort_merge.add_loop("merge", "merge_label1")
sort_merge.add_loop("merge", "merge_label2")
sort_merge.add_loop("merge", "merge_label3")
sort_merge.add_loop("ms_mergesort", "mergesort_label1")
sort_merge.add_loop("ms_mergesort", "mergesort_label2")
sort_merge.add_required_files(["input.data", "check.data"])
sort_merge.set_exec_cmd("sort_merge-gem5-accel")

sort_radix = Benchmark("sort_radix", "sort/radix")
sort_radix.set_kernels(["ss_sort"])
sort_radix.set_main_id(0x000000E0)
sort_radix.add_array("a", 2048, 4)
sort_radix.add_array("b", 2048, 4)
sort_radix.add_array("bucket", 2048, 4)
sort_radix.add_array("sum", 128, 4)
sort_radix.add_loop("last_step_scan", "last_1")
sort_radix.add_loop("last_step_scan", "last_2")
sort_radix.add_loop("local_scan", "local_1")
sort_radix.add_loop("local_scan", "local_2")
sort_radix.add_loop("sum_scan", "sum_1")
sort_radix.add_loop("hist", "hist_1")
sort_radix.add_loop("hist", "hist_2")
sort_radix.add_loop("update", "update_1")
sort_radix.add_loop("update", "update_2")
sort_radix.add_loop("init", "init_1")
sort_radix.add_loop("ss_sort", "sort_1")
sort_radix.add_required_files(["input.data", "check.data"])
sort_radix.set_exec_cmd("sort_radix-gem5-accel")

spmv_crs = Benchmark("spmv_crs", "spmv/crs")
spmv_crs.set_kernels(["spmv"])
spmv_crs.set_main_id(0x000000F0)
spmv_crs.add_array("val", 1666, 8)
spmv_crs.add_array("cols", 1666, 4)
spmv_crs.add_array("rowDelimiters", 495, 4)
spmv_crs.add_array("vec", 494, 8)
spmv_crs.add_array("out", 494, 8)
spmv_crs.add_loop("spmv", "spmv_1")
spmv_crs.add_loop("spmv", "spmv_2")
spmv_crs.add_required_files(["input.data", "check.data"])
spmv_crs.set_exec_cmd("spmv_crs-gem5-accel")

spmv_ellpack = Benchmark("spmv_ellpack", "spmv/ellpack")
spmv_ellpack.set_kernels(["ellpack"])
spmv_ellpack.set_main_id(0x00000100)
spmv_ellpack.add_array("nzval", 4940, 8)
spmv_ellpack.add_array("cols", 4940, 4)
spmv_ellpack.add_array("vec", 494, 8)
spmv_ellpack.add_array("out", 494, 8)
spmv_ellpack.add_loop("ellpack", "ellpack_1")
spmv_ellpack.add_loop("ellpack", "ellpack_2")
spmv_ellpack.add_required_files(["input.data", "check.data"])
spmv_ellpack.set_exec_cmd("spmv_ellpack-gem5-accel")

stencil_stencil2d = Benchmark("stencil_stencil2d", "stencil/stencil2d")
stencil_stencil2d.set_kernels(["stencil"])
stencil_stencil2d.set_main_id(0x00000110)
stencil_stencil2d.add_array("orig", 8192, 4)
stencil_stencil2d.add_array("sol", 8192, 4)
stencil_stencil2d.add_array("filter", 9, 4)
stencil_stencil2d.add_loop("stencil", "stencil_label1")
stencil_stencil2d.add_loop("stencil", "stencil_label2")
stencil_stencil2d.add_loop("stencil", "stencil_label3")
stencil_stencil2d.add_loop("stencil", "stencil_label4")
stencil_stencil2d.add_required_files(["input.data", "check.data"])
stencil_stencil2d.set_exec_cmd("stencil_stencil2d-gem5-accel")

stencil_stencil3d = Benchmark("stencil_stencil3d", "stencil/stencil3d")
stencil_stencil3d.set_kernels(["stencil3d"])
stencil_stencil3d.set_main_id(0x00000120)
stencil_stencil3d.add_array("orig", 16384, 4)
stencil_stencil3d.add_array("sol", 16384, 4)
stencil_stencil3d.add_array("C", 2, 4)
stencil_stencil3d.add_loop("stencil3d", "height_bound_col")
stencil_stencil3d.add_loop("stencil3d", "height_bound_row")
stencil_stencil3d.add_loop("stencil3d", "col_bound_height")
stencil_stencil3d.add_loop("stencil3d", "col_bound_row")
stencil_stencil3d.add_loop("stencil3d", "row_bound_height")
stencil_stencil3d.add_loop("stencil3d", "row_bound_col")
stencil_stencil3d.add_loop("stencil3d", "loop_height")
stencil_stencil3d.add_loop("stencil3d", "loop_col")
stencil_stencil3d.add_loop("stencil3d", "loop_row")
stencil_stencil3d.add_required_files(["input.data", "check.data"])
stencil_stencil3d.set_exec_cmd("stencil_stencil3d-gem5-accel")

viterbi_viterbi = Benchmark("viterbi_viterbi", "viterbi/viterbi")
viterbi_viterbi.set_kernels(["viterbi"])
viterbi_viterbi.set_main_id(0x00000130)
viterbi_viterbi.add_array("obs", 140, 1)
viterbi_viterbi.add_array("init", 64, 8)
viterbi_viterbi.add_array("transition", 4096, 8)
viterbi_viterbi.add_array("emission", 4096, 8)
viterbi_viterbi.add_array("path", 140, 1)
viterbi_viterbi.add_array("llike", 4096, 8)
viterbi_viterbi.add_loop("viterbi", "L_init")
viterbi_viterbi.add_loop("viterbi", "L_timestep")
viterbi_viterbi.add_loop("viterbi", "L_curr_state")
viterbi_viterbi.add_loop("viterbi", "L_prev_state")
viterbi_viterbi.add_loop("viterbi", "L_end")
viterbi_viterbi.add_required_files(["input.data", "check.data"])
viterbi_viterbi.set_exec_cmd("viterbi_viterbi-gem5-accel")
