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
from gnuradio import zeromq
import sip



class task3(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "task3")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.skip = skip = 0
        self.shift = shift = 0.2
        self.noise_amp = noise_amp = 0.1
        self.consti = consti = digital.constellation_calcdist([-1-1j, -1+1j, 1-1j, 1+1j], [0, 1, 2, 3],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.consti.set_npwr(1.0)
        self.alpha = alpha = 1

        ##################################################
        # Blocks
        ##################################################

        self._shift_range = qtgui.Range(0, 10, 0.1, 0.2, 200)
        self._shift_win = qtgui.RangeWidget(self._shift_range, self.set_shift, "'shift'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._shift_win)
        self._noise_amp_range = qtgui.Range(0, 1, 0.1, 0.1, 200)
        self._noise_amp_win = qtgui.RangeWidget(self._noise_amp_range, self.set_noise_amp, "'noise_amp'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_amp_win)
        self._alpha_range = qtgui.Range(0, 1, 0.1, 1, 200)
        self._alpha_win = qtgui.RangeWidget(self._alpha_range, self.set_alpha, "'alpha'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_float, 1, 'tcp://127.0.0.1:5555', 100, False, (-1), True)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_float, 1, 'tcp://127.0.0.1:5555', 100, False, (-1), False)
        self._skip_range = qtgui.Range(0, 7, 1, 0, 200)
        self._skip_win = qtgui.RangeWidget(self._skip_range, self.set_skip, "'skip'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._skip_win)
        self.root_raised_cosine_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                400000,
                50000,
                alpha,
                88))
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                400000,
                50000,
                alpha,
                88))
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                400000,
                50000,
                alpha,
                88))
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            400000, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_const_sink_x_2 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_2.set_update_time(0.10)
        self.qtgui_const_sink_x_2.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_2.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_2.enable_autoscale(False)
        self.qtgui_const_sink_x_2.enable_grid(False)
        self.qtgui_const_sink_x_2.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_2_win = sip.wrapinstance(self.qtgui_const_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_2_win)
        self.low_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                8000000,
                50000,
                5000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                8000000,
                50000,
                5000,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(8, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.iir_filter_xxx_0_0 = filter.iir_filter_ffd([0.01], [-1, 0.99], True)
        self.iir_filter_xxx_0 = filter.iir_filter_ffd([1.0001,-1], [-1,1], True)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(consti)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([-1-1j, -1+1j, 1-1j, 1+1j], 1)
        self.blocks_vco_c_0 = blocks.vco_c(50000, (-5), 1)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_1_1 = blocks.threshold_ff((-0.001), 0.001, 0)
        self.blocks_threshold_ff_1_0_0 = blocks.threshold_ff((-0.001), 0.001, 0)
        self.blocks_sub_xx_1_1 = blocks.sub_ff(1)
        self.blocks_sub_xx_1_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 3)
        self.blocks_pack_k_bits_bb_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(2)
        self.blocks_multiply_xx_1_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(1.414)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_ff(1.414)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'Original_Text.txt', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'output2.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 100)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(8000000, analog.GR_COS_WAVE, (500000+shift), 1, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(8000000, analog.GR_SIN_WAVE, (500000+shift), 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(8000000, analog.GR_SIN_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(8000000, analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_amp, 0)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0.707)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0.707)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_sub_xx_1_0_0, 1))
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_sub_xx_1_1, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_1_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_1_1, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_threshold_ff_1_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_threshold_ff_1_1, 0))
        self.connect((self.blocks_complex_to_imag_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_sub_xx_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_sub_xx_1_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.qtgui_const_sink_x_2, 0))
        self.connect((self.blocks_multiply_xx_1_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_1_1, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.iir_filter_xxx_0_0, 0))
        self.connect((self.blocks_sub_xx_1_0_0, 0), (self.blocks_multiply_xx_1_0_0, 1))
        self.connect((self.blocks_sub_xx_1_1, 0), (self.blocks_multiply_xx_1_1, 0))
        self.connect((self.blocks_threshold_ff_1_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_threshold_ff_1_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_pack_k_bits_bb_1, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_float_to_complex_1, 1))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.iir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.iir_filter_xxx_0_0, 0), (self.zeromq_push_sink_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_imag_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.root_raised_cosine_filter_0_1, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_1, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.zeromq_pull_source_0, 0), (self.blocks_delay_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_skip(self):
        return self.skip

    def set_skip(self, skip):
        self.skip = skip

    def get_shift(self):
        return self.shift

    def set_shift(self, shift):
        self.shift = shift
        self.analog_sig_source_x_0_0_0.set_frequency((500000+self.shift))
        self.analog_sig_source_x_0_1.set_frequency((500000+self.shift))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_noise_source_x_0.set_amplitude(self.noise_amp)

    def get_consti(self):
        return self.consti

    def set_consti(self, consti):
        self.consti = consti
        self.digital_constellation_decoder_cb_0.set_constellation(self.consti)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, 400000, 50000, self.alpha, 88))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(3, 400000, 50000, self.alpha, 88))
        self.root_raised_cosine_filter_0_1.set_taps(firdes.root_raised_cosine(3, 400000, 50000, self.alpha, 88))




def main(top_block_cls=task3, options=None):

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
