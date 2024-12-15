#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
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
import sip



class task3_qpsk_modulation(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "task3_qpsk_modulation")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist([1+0j, 0.707+0.707j, 0+1j, -0.707+0.707j, -1+0j, -0.707-0.707j, 0-1j, 0.707-0.707j], [0, 1, 2, 3, 4, 5, 6, 7],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.variable_constellation_0.set_npwr(1.0)
        self.symbol_rate = symbol_rate = 10000
        self.sps = sps = 8
        self.skip = skip = 2
        self.samp_rate = samp_rate = 80000
        self.noise_amp = noise_amp = 0.1
        self.delay = delay = 3
        self.alpha = alpha = 0.5

        ##################################################
        # Blocks
        ##################################################

        self._noise_amp_range = qtgui.Range(0, 1, 0.01, 0.1, 200)
        self._noise_amp_win = qtgui.RangeWidget(self._noise_amp_range, self.set_noise_amp, "'noise_amp'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_amp_win)
        self._delay_range = qtgui.Range(0, 20, 1, 3, 200)
        self._delay_win = qtgui.RangeWidget(self._delay_range, self.set_delay, "'delay'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_win)
        self._alpha_range = qtgui.Range(0, 1, 0.01, 0.5, 200)
        self._alpha_win = qtgui.RangeWidget(self._alpha_range, self.set_alpha, "'alpha'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)
        self._skip_range = qtgui.Range(0, 500, 1, 2, 200)
        self._skip_win = qtgui.RangeWidget(self._skip_range, self.set_skip, "'skip'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._skip_win)
        self.root_raised_cosine_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                samp_rate,
                symbol_rate,
                alpha,
                (11*sps)))
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                samp_rate,
                symbol_rate,
                alpha,
                (11*sps)))
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                samp_rate,
                symbol_rate,
                alpha,
                (11*sps)))
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=5,
                taps=[],
                fractional_bw=0)
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
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_eye_sink_x_0 = qtgui.eye_sink_f(
            1024, #size
            samp_rate, #samp_rate
            1, #number of inputs
            None
        )
        self.qtgui_eye_sink_x_0.set_update_time(0.10)
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(sps)
        self.qtgui_eye_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_eye_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_eye_sink_x_0.enable_tags(True)
        self.qtgui_eye_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_eye_sink_x_0.enable_autoscale(False)
        self.qtgui_eye_sink_x_0.enable_grid(False)
        self.qtgui_eye_sink_x_0.enable_axis_labels(True)
        self.qtgui_eye_sink_x_0.enable_control_panel(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'blue', 'blue', 'blue', 'blue',
            'blue', 'blue', 'blue', 'blue', 'blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_eye_sink_x_0.set_line_label(i, "Eye[Data {0}]".format(i))
            else:
                self.qtgui_eye_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_eye_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_eye_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_eye_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_eye_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_eye_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_eye_sink_x_0_win = sip.wrapinstance(self.qtgui_eye_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_eye_sink_x_0_win)
        self.low_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                (samp_rate*5),
                50000,
                200,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                (samp_rate*5),
                50000,
                200,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(8, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_constellation_decoder_cb_1 = digital.constellation_decoder_cb(variable_constellation_0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([1+0j, 0.707+0.707j, 0+1j, -0.707+0.707j, -1+0j, -0.707-0.707j, 0-1j, 0.707-0.707j], 1)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(3)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_0_0 = blocks.threshold_ff((-0.0500), 0.0500, 0)
        self.blocks_threshold_ff_0 = blocks.threshold_ff((-0.0500), 0.0500, 0)
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_char*1, 25)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(3)
        self.blocks_multiply_xx_0_0_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1000, 1, 4000, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'demo.txt', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'output_khari_8psk.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, delay)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, delay)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f((samp_rate*5), analog.GR_SIN_WAVE, 100000, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f((samp_rate*5), analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_noise_source_x_1 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_amp, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_1, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0_1, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_1_0, 0))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_0_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_0_1_0, 1))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_complex_to_imag_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_eye_sink_x_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.digital_constellation_decoder_cb_1, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_xx_0_0_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_1_0, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_threshold_ff_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_1, 0), (self.blocks_skiphead_0_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_threshold_ff_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_imag_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.root_raised_cosine_filter_0_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0_0, 0), (self.blocks_delay_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task3_qpsk_modulation")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0
        self.digital_constellation_decoder_cb_1.set_constellation(self.variable_constellation_0)

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(self.sps)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))

    def get_skip(self):
        return self.skip

    def set_skip(self, skip):
        self.skip = skip

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq((self.samp_rate*5))
        self.analog_sig_source_x_0_0_0.set_sampling_freq((self.samp_rate*5))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, (self.samp_rate*5), 50000, 200, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, (self.samp_rate*5), 50000, 200, window.WIN_HAMMING, 6.76))
        self.qtgui_eye_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_1.set_amplitude(self.noise_amp)

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.blocks_delay_0.set_dly(int(self.delay))
        self.blocks_delay_0_0.set_dly(int(self.delay))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))
        self.root_raised_cosine_filter_0_0_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, self.symbol_rate, self.alpha, (11*self.sps)))




def main(top_block_cls=task3_qpsk_modulation, options=None):

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
