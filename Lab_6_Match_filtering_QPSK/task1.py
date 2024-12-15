#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: khariwal
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



class task1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "task1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 10000
        self.sps = sps = 8
        self.skip_head = skip_head = 4
        self.samp_rate = samp_rate = 80000
        self.noise_amp = noise_amp = 0.1
        self.delay_value = delay_value = 4
        self.alpha = alpha = 0.5

        ##################################################
        # Blocks
        ##################################################

        self._skip_head_range = qtgui.Range(0, 10, 1, 4, 200)
        self._skip_head_win = qtgui.RangeWidget(self._skip_head_range, self.set_skip_head, "'skip_head'", "counter", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._skip_head_win)
        self._noise_amp_range = qtgui.Range(0, 1, 0.1, 0.1, 200)
        self._noise_amp_win = qtgui.RangeWidget(self._noise_amp_range, self.set_noise_amp, "'noise_amp'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_amp_win)
        self._alpha_range = qtgui.Range(0, 1, 0.01, 0.5, 200)
        self._alpha_win = qtgui.RangeWidget(self._alpha_range, self.set_alpha, "alpha", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)
        self.root_raised_cosine_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                (sps*symbol_rate),
                symbol_rate,
                alpha,
                (11*sps)))
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                (sps*symbol_rate),
                symbol_rate,
                alpha,
                (11*sps)))
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=5,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=5,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                (samp_rate*5),
                50000,
                200,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(sps, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(sps, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([-1,1], 1)
        self._delay_value_range = qtgui.Range(0, 10, 1, 4, 200)
        self._delay_value_win = qtgui.RangeWidget(self._delay_value_range, self.set_delay_value, "'delay_value'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_value_win)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_0 = blocks.threshold_ff((-0.0100), 0.0100, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, skip_head)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar(1, 1, 0)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'Original_Text.txt', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'output_khari_task2.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, 4)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1 = analog.sig_source_f((samp_rate*5), analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f((samp_rate*5), analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_amp, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_delay_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))

    def get_skip_head(self):
        return self.skip_head

    def set_skip_head(self, skip_head):
        self.skip_head = skip_head

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq((self.samp_rate*5))
        self.analog_sig_source_x_1.set_sampling_freq((self.samp_rate*5))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, (self.samp_rate*5), 50000, 200, window.WIN_HAMMING, 6.76))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)

    def get_delay_value(self):
        return self.delay_value

    def set_delay_value(self, delay_value):
        self.delay_value = delay_value

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))




def main(top_block_cls=task1, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
