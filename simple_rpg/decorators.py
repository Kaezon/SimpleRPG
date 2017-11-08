"""Decorators for use with SimpleRPG"""
import logging

logger = logging.getLogger('SimpleRPG')


def must_have_character(ctx):
    logger.info("The decorator has executed.")
    logger.info("CTX: {}".format(ctx))
