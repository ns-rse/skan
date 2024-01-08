import numpy as np

from skan._testdata import skeleton1
from skan import Skeleton, summarize


def test_find_main():
    skeleton = Skeleton(skeleton1)
    summary_df = summarize(skeleton, find_main_branch=True, separator='_')

    non_main_edge_start = [2, 1]
    non_main_edge_finish = [3, 3]

    non_main_df = summary_df.loc[summary_df['main'] == False]
    assert non_main_df.shape[0] == 1
    coords = non_main_df[[
            'coord_src_0', 'coord_src_1', 'coord_dst_0', 'coord_dst_1'
            ]].to_numpy()
    assert (
            np.all(coords == non_main_edge_start + non_main_edge_finish)
            or np.all(coords == non_main_edge_finish + non_main_edge_start)
            )
